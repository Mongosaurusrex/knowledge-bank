"""
pipeline.py

End-to-end pipeline: reads all *.md files under a sources directory,
cleans markdown, runs SemanticChunker, and writes JSONL chunks to an
output file with full provenance metadata.

Usage:
    python pipeline.py [--sources sources] [--output knowledge/chunks.jsonl]
                       [--threshold 0.5] [--min 100] [--max 2000]
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterator

from semantic_chunker import SemanticChunker


# ---------------------------------------------------------------------------
# Markdown preprocessor
# ---------------------------------------------------------------------------

class MarkdownPreprocessor:
    """
    Converts a markdown document into a list of (heading, clean_text) pairs
    so the chunker operates on prose rather than raw markdown syntax.
    """

    _CALLOUT_HEADER = re.compile(r'^\s*>\s*\[!.*?\]\s*$', re.IGNORECASE)
    _BLOCKQUOTE     = re.compile(r'^\s*>\s?')
    _DISPLAY_MATH   = re.compile(r'\$\$.*?\$\$', re.DOTALL)
    _INLINE_MATH    = re.compile(r'\$[^$\n]+?\$')
    _CODE_FENCE     = re.compile(r'```.*?```', re.DOTALL)
    _BOLD_ITALIC    = re.compile(r'(\*{1,3}|_{1,3})(.*?)\1')
    _WIKILINK       = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')
    _MDLINK         = re.compile(r'\[([^\]]+)\]\([^)]+\)')
    _SLUG           = re.compile(r'^Slug:\s+.+$', re.MULTILINE)
    _HEADING        = re.compile(r'^(#{1,6})\s+(.+)$')
    _HR             = re.compile(r'^[-*_]{3,}\s*$')

    def process(self, text: str) -> list[tuple[str, str]]:
        """
        Returns a list of (section_heading, clean_prose) pairs.
        One entry per markdown section (split on any heading level).
        """
        # Strip slug metadata
        text = self._SLUG.sub('', text)

        # Strip code fences before anything else
        text = self._CODE_FENCE.sub('', text)

        # Replace display math blocks with a placeholder sentence so the
        # chunker treats them as a single logical unit rather than noise
        text = self._DISPLAY_MATH.sub('[equation]', text)

        lines = text.split('\n')
        sections: list[tuple[str, list[str]]] = []
        current_heading = ''
        buffer: list[str] = []

        def flush():
            prose = self._lines_to_prose(buffer)
            if prose:
                sections.append((current_heading, prose))

        for line in lines:
            # Horizontal rules: just skip
            if self._HR.match(line):
                continue

            # Heading → start new section
            m = self._HEADING.match(line)
            if m:
                flush()
                buffer = []
                current_heading = self._clean_inline(m.group(2))
                continue

            # Skip callout header lines like "> [!note]"
            if self._CALLOUT_HEADER.match(line):
                continue

            # Strip blockquote markers but keep content
            line = self._BLOCKQUOTE.sub('', line)

            # Strip bullet/numbered-list markers, keep text
            line = re.sub(r'^\s*[-*+]\s+', '', line)
            line = re.sub(r'^\s*\d+[.)]\s+', '', line)

            # Strip inline formatting
            line = self._clean_inline(line)

            stripped = line.strip()
            if stripped:
                buffer.append(stripped)

        flush()
        return sections

    def _clean_inline(self, text: str) -> str:
        text = self._BOLD_ITALIC.sub(r'\2', text)
        text = self._INLINE_MATH.sub('[expr]', text)
        text = self._WIKILINK.sub(r'\1', text)
        text = self._MDLINK.sub(r'\1', text)
        # Collapse extra whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def _lines_to_prose(self, lines: list[str]) -> str:
        """Join buffered lines into prose, inserting spaces between items."""
        return ' '.join(lines).strip()


# ---------------------------------------------------------------------------
# Chunk dataclass
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    source: str        # path relative to workspace root
    title: str         # document title (first # heading or filename stem)
    section: str       # nearest section heading
    chunk_index: int   # per-document sequential index
    text: str          # clean prose chunk text


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

class Pipeline:
    def __init__(
        self,
        sources_dir: str = 'sources',
        output_path: str = 'knowledge/chunks.jsonl',
        similarity_threshold: float = 0.5,
        min_chunk_size: int = 100,
        max_chunk_size: int = 2000,
    ):
        self.sources_dir = Path(sources_dir)
        self.output_path = Path(output_path)
        self.preprocessor = MarkdownPreprocessor()
        self.chunker = SemanticChunker(
            similarity_threshold=similarity_threshold,
            min_chunk_size=min_chunk_size,
            max_chunk_size=max_chunk_size,
        )

    def _extract_title(self, text: str, file_path: Path) -> str:
        for line in text.split('\n')[:10]:
            if line.startswith('# '):
                return line.lstrip('# ').strip()
        return file_path.stem

    def _iter_files(self) -> Iterator[Path]:
        yield from sorted(self.sources_dir.rglob('*.md'))

    def process_file(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding='utf-8')
        title = self._extract_title(text, file_path)
        source = str(file_path)

        sections = self.preprocessor.process(text)

        chunks: list[Chunk] = []
        chunk_index = 0

        for heading, prose in sections:
            if not prose:
                continue

            raw_chunks = self.chunker.chunk(prose)

            for chunk_text in raw_chunks:
                if not chunk_text.strip():
                    continue
                chunks.append(Chunk(
                    source=source,
                    title=title,
                    section=heading or title,
                    chunk_index=chunk_index,
                    text=chunk_text.strip(),
                ))
                chunk_index += 1

        return chunks

    def run(self) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        total_files = 0
        total_chunks = 0
        skipped = 0

        with self.output_path.open('w', encoding='utf-8') as out:
            for file_path in self._iter_files():
                try:
                    chunks = self.process_file(file_path)
                except Exception as exc:
                    print(f"  [skip] {file_path}: {exc}", file=sys.stderr)
                    skipped += 1
                    continue

                for chunk in chunks:
                    out.write(json.dumps(asdict(chunk), ensure_ascii=False) + '\n')

                total_files += 1
                total_chunks += len(chunks)
                print(f"  {file_path.relative_to(self.sources_dir)}  →  {len(chunks)} chunks")

        print(
            f"\nDone. {total_files} files, {total_chunks} chunks "
            f"→ {self.output_path}  (skipped {skipped})"
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Semantic chunking pipeline for knowledge-bank')
    parser.add_argument('--sources',   default='sources',                help='Root folder to crawl for .md files')
    parser.add_argument('--output',    default='knowledge/chunks.jsonl', help='Output JSONL path')
    parser.add_argument('--threshold', type=float, default=0.5,          help='Cosine similarity split threshold')
    parser.add_argument('--min',       type=int,   default=100,          help='Min chunk size in chars')
    parser.add_argument('--max',       type=int,   default=2000,         help='Max chunk size in chars')
    args = parser.parse_args()

    pipeline = Pipeline(
        sources_dir=args.sources,
        output_path=args.output,
        similarity_threshold=args.threshold,
        min_chunk_size=args.min,
        max_chunk_size=args.max,
    )
    pipeline.run()


if __name__ == '__main__':
    main()
