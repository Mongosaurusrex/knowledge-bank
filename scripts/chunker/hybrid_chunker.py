# hybrid_chunker.py
# Combines structural and embedding-based chunking for best results

from semantic_chunker import SemanticChunker
from structural_chunker import StructuralChunker
from typing import List, Iterable
import re


class HybridChunker:
    """
    Two-pass chunking strategy:
    1. Structural pass identifies obvious boundaries (headings, paragraphs)
    2. Embedding pass refines large sections into semantic units

    This approach is faster than pure embedding while more accurate than
    pure structural analysis.
    """

    def __init__(
        self,
        embedding_model: str = "all-MiniLM-L6-v2",
        similarity_threshold: float = 0.5,
        min_chunk_size: int = 150,
        max_chunk_size: int = 1500,
        embedding_refinement_threshold: int = 800,
        token_aware: bool = False,
        target_tokens: int = 800,
        overlap_tokens: int = 100,
        encoding_name: str = "cl100k_base",
    ):
        # Structural chunker for first pass
        self.structural = StructuralChunker(
            min_chunk_size=min_chunk_size,
            max_chunk_size=max_chunk_size * 2,  # Allow larger initial chunks
            boundary_threshold=0.7
        )

        # Semantic chunker for refinement
        self.semantic = SemanticChunker(
            model_name=embedding_model,
            similarity_threshold=similarity_threshold,
            min_chunk_size=min_chunk_size,
            max_chunk_size=max_chunk_size
        )

        # Only refine chunks larger than this
        self.refinement_threshold = embedding_refinement_threshold

        # Final size limits
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size

        # Optional token-aware post-processing (OpenAI embedding-friendly)
        self.token_aware = token_aware
        self.target_tokens = target_tokens
        self.overlap_tokens = overlap_tokens
        self.encoding_name = encoding_name
        self._encoding = None

        # Removes heading/list artifacts like @@### while preserving normal markdown.
        self._leading_artifact = re.compile(r'^\s*@@(?=(#{1,6}\s|[-*+]\s|\d+[.)]\s))')

    def chunk(self, text: str) -> List[str]:
        """
        Process document through structural then semantic chunking.
        """
        text = self._clean_markdown_noise(text)

        # Pass 1: Structural chunking (fast, catches obvious breaks)
        structural_chunks = self.structural.chunk(text)

        # Pass 2: Refine large chunks with embedding analysis
        final_chunks = []

        for chunk in structural_chunks:
            if len(chunk) > self.refinement_threshold:
                # This chunk is large enough to potentially contain
                # multiple semantic topics - refine it
                refined = self.semantic.chunk(chunk)
                final_chunks.extend(refined)
            else:
                final_chunks.append(chunk)

        # Pass 3: Merge any chunks that ended up too small
        merged = self.merge_small_chunks(final_chunks)

        # Optional Pass 4: enforce token budget + overlap safely.
        if self.token_aware:
            return self._token_aware_postprocess(merged)

        return merged

    def _get_encoding(self):
        if self._encoding is not None:
            return self._encoding

        try:
            import tiktoken
        except ImportError as exc:
            raise ImportError(
                "token_aware=True requires tiktoken. Install with: pip install tiktoken"
            ) from exc

        self._encoding = tiktoken.get_encoding(self.encoding_name)
        return self._encoding

    def _count_tokens(self, text: str) -> int:
        enc = self._get_encoding()
        return len(enc.encode(text))

    def _token_tail(self, text: str, token_count: int) -> str:
        if token_count <= 0:
            return ""
        enc = self._get_encoding()
        ids = enc.encode(text)
        if not ids:
            return ""
        return enc.decode(ids[-token_count:]).strip()

    def _clean_markdown_noise(self, text: str) -> str:
        lines = text.split("\n")
        cleaned = [self._leading_artifact.sub("", line) for line in lines]
        return "\n".join(cleaned).strip()

    # Matches a GFM separator row: | --- | :---: | --- |
    _TABLE_SEP = re.compile(r'^\|[-:| ]+\|$')

    def _is_table_line(self, line: str) -> bool:
        stripped = line.strip()
        # Require at least 2 pipes AND the line must start or end with '|'
        # so that LaTeX \left|...\right|, absolute-value expressions, and
        # logical-OR operators are not mistaken for GFM table rows.
        return stripped.count("|") >= 2 and (stripped.startswith("|") or stripped.endswith("|"))

    def _is_table_separator(self, line: str) -> bool:
        return bool(self._TABLE_SEP.match(line.strip()))

    def _table_has_header(self, table_text: str) -> bool:
        """Return True when the table block contains a GFM separator row."""
        return any(self._is_table_separator(l) for l in table_text.split("\n"))

    def _extract_table_header(self, table_text: str) -> str:
        """Return the header row(s) + separator row from a well-formed table."""
        rows = [r for r in table_text.split("\n") if r.strip()]
        for i, row in enumerate(rows):
            if self._is_table_separator(row):
                return "\n".join(rows[: i + 1])
        # Fallback: assume first two rows are header + separator
        return "\n".join(rows[:2]) if len(rows) >= 2 else (rows[0] if rows else "")

    def _split_blocks_preserve_tables(self, text: str) -> List[dict]:
        lines = text.split("\n")
        blocks: List[dict] = []
        i = 0

        while i < len(lines):
            if self._is_table_line(lines[i]):
                start = i
                i += 1
                while i < len(lines) and self._is_table_line(lines[i]):
                    i += 1
                table_text = "\n".join(lines[start:i]).strip()
                if table_text:
                    blocks.append({"kind": "table", "text": table_text})
                continue

            start = i
            i += 1
            while i < len(lines) and not self._is_table_line(lines[i]):
                i += 1
            text_block = "\n".join(lines[start:i]).strip()
            if text_block:
                blocks.append({"kind": "text", "text": text_block})

        return blocks

    def _split_on_header(self, text: str) -> List[str]:
        matches = list(re.finditer(r'\n###\s', text))
        if not matches:
            return [text]

        indices = [0] + [m.start() + 1 for m in matches] + [len(text)]
        parts: List[str] = []
        for a, b in zip(indices, indices[1:]):
            part = text[a:b].strip()
            if part:
                parts.append(part)
        return parts

    def _split_by_separator(self, text: str, sep: str) -> List[str]:
        if sep == " ":
            parts = [p for p in text.split(" ") if p]
        else:
            parts = [p for p in text.split(sep) if p.strip()]
        return parts if parts else [text]

    def _join_units(self, units: Iterable[str], sep: str) -> str:
        if sep == " ":
            return " ".join(u.strip() for u in units if u.strip()).strip()
        return sep.join(u for u in units if u).strip()

    def _hard_split_by_tokens(self, text: str) -> List[str]:
        enc = self._get_encoding()
        ids = enc.encode(text)
        if len(ids) <= self.target_tokens:
            return [text.strip()] if text.strip() else []

        parts: List[str] = []
        for i in range(0, len(ids), self.target_tokens):
            piece = enc.decode(ids[i:i + self.target_tokens]).strip()
            if piece:
                parts.append(piece)
        return parts

    def _recursive_text_split(self, text: str, level: int = 0) -> List[str]:
        text = text.strip()
        if not text:
            return []
        if self._count_tokens(text) <= self.target_tokens:
            return [text]

        split_plan = [
            ("header", None),
            ("sep", "\n\n"),
            ("sep", "\n"),
            ("sep", " "),
        ]

        if level >= len(split_plan):
            return self._hard_split_by_tokens(text)

        mode, sep = split_plan[level]
        if mode == "header":
            units = self._split_on_header(text)
            join_sep = "\n"
        else:
            units = self._split_by_separator(text, sep)
            join_sep = sep

        if len(units) == 1:
            return self._recursive_text_split(text, level + 1)

        packed: List[str] = []
        buf: List[str] = []
        for unit in units:
            candidate = self._join_units(buf + [unit], join_sep)
            if buf and self._count_tokens(candidate) > self.target_tokens:
                packed.append(self._join_units(buf, join_sep))
                buf = [unit]
            else:
                buf.append(unit)
        if buf:
            packed.append(self._join_units(buf, join_sep))

        out: List[str] = []
        for piece in packed:
            if self._count_tokens(piece) <= self.target_tokens:
                out.append(piece)
            else:
                out.extend(self._recursive_text_split(piece, level + 1))

        return [p.strip() for p in out if p.strip()]

    def _split_table_block(self, table_text: str) -> List[str]:
        if self._count_tokens(table_text) <= self.target_tokens:
            return [table_text.strip()]

        rows = [r for r in table_text.split("\n") if r.strip()]
        if len(rows) < 3:
            return self._hard_split_by_tokens(table_text)

        # Find where the separator row is so we correctly identify the header.
        sep_idx = next(
            (i for i, r in enumerate(rows) if self._is_table_separator(r)), 1
        )
        header = rows[: sep_idx + 1]   # everything up to and including separator
        data_rows = rows[sep_idx + 1 :]

        chunks: List[str] = []
        current_rows: List[str] = []

        for row in data_rows:
            if not current_rows:
                trial_rows = header + [row]
            else:
                trial_rows = header + current_rows + [row]

            trial_text = "\n".join(trial_rows)
            if current_rows and self._count_tokens(trial_text) > self.target_tokens:
                chunks.append("\n".join(header + current_rows).strip())
                current_rows = [row]
            else:
                current_rows.append(row)

        if current_rows:
            chunks.append("\n".join(header + current_rows).strip())

        fixed: List[str] = []
        for chunk in chunks:
            if self._count_tokens(chunk) <= self.target_tokens:
                fixed.append(chunk)
            else:
                fixed.extend(self._hard_split_by_tokens(chunk))

        return fixed

    def _token_aware_postprocess(self, chunks: List[str]) -> List[str]:
        # Produce tagged pieces so tables are kept strictly separate.
        # Each entry: (kind, text, table_header_or_None)
        tagged: List[tuple] = []

        for chunk in chunks:
            blocks = self._split_blocks_preserve_tables(chunk)
            for block in blocks:
                if block["kind"] == "table":
                    tbl = block["text"]
                    if self._table_has_header(tbl):
                        # Well-formed table — extract header for continuations.
                        hdr = self._extract_table_header(tbl)
                        for t in self._split_table_block(tbl):
                            tagged.append(("table", t, hdr))
                    else:
                        # Continuation fragment — header will be filled in below.
                        tagged.append(("table", tbl, None))
                else:
                    for t in self._recursive_text_split(block["text"]):
                        tagged.append(("text", t, None))

        # Forward-fill missing table headers from the most recently seen header.
        last_header: str = ""
        resolved: List[tuple] = []
        for kind, piece, hdr in tagged:
            if kind == "table":
                if hdr:
                    last_header = hdr
                elif last_header:
                    # Prepend the saved header to make this chunk self-describing.
                    piece = (last_header + "\n" + piece).strip()
                    hdr = last_header
            else:
                last_header = ""  # Reset when we leave a table context.
            resolved.append((kind, piece, hdr))

        out: List[str] = []
        current_kind: str = ""
        current: str = ""
        current_hdr: str = ""

        for kind, piece, hdr in resolved:
            if not current:
                current = piece
                current_kind = kind
                current_hdr = hdr or ""
                continue

            # Never merge text and table pieces into the same chunk.
            if kind != current_kind:
                out.append(current.strip())
                current = piece
                current_kind = kind
                current_hdr = hdr or ""
                continue

            candidate = (current + "\n\n" + piece).strip()
            if self._count_tokens(candidate) <= self.target_tokens:
                current = candidate
                continue

            out.append(current.strip())
            if kind == "text":
                # Only text chunks get an overlap tail from the previous chunk.
                overlap = self._token_tail(current, self.overlap_tokens)
                current = (overlap + "\n\n" + piece).strip() if overlap else piece
            else:
                # Table chunks are self-describing via their header rows;
                # never inject overlap text before a table row.
                current = piece
            current_kind = kind
            current_hdr = hdr or ""

            if self._count_tokens(current) > self.target_tokens:
                subpieces = self._hard_split_by_tokens(current)
                if subpieces:
                    out.extend(subpieces[:-1])
                    current = subpieces[-1]

        if current.strip():
            out.append(current.strip())

        return out

    def merge_small_chunks(self, chunks: List[str]) -> List[str]:
        """
        Merge undersized chunks with neighbors when possible.
        """
        if len(chunks) <= 1:
            return chunks

        merged = []
        buffer = chunks[0]

        for chunk in chunks[1:]:
            if len(buffer) < self.min_chunk_size:
                combined = buffer + "\n\n" + chunk
                if len(combined) <= self.max_chunk_size:
                    buffer = combined
                else:
                    merged.append(buffer)
                    buffer = chunk
            else:
                merged.append(buffer)
                buffer = chunk

        merged.append(buffer)
        return merged

    def chunk_with_metadata(self, text: str) -> List[dict]:
        """
        Returns chunks with additional metadata for debugging and analysis.
        """
        chunks = self.chunk(text)

        results = []
        char_offset = 0

        for i, chunk in enumerate(chunks):
            # Find actual position in original text
            start_pos = text.find(chunk[:50], char_offset)
            if start_pos == -1:
                start_pos = char_offset

            results.append({
                'index': i,
                'text': chunk,
                'char_count': len(chunk),
                'word_count': len(chunk.split()),
                'start_position': start_pos,
                'preview': chunk[:100] + '...' if len(chunk) > 100 else chunk
            })

            char_offset = start_pos + len(chunk)

        return results