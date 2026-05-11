from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer


class ChunkEvaluator:
    """
    Evaluate chunk quality using multiple metrics.

    Good chunks should:
    - Have high internal coherence (sentences within chunk are related)
    - Have low inter-chunk similarity (chunks cover distinct topics)
    - Stay within size bounds
    - Preserve important boundaries
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def evaluate(self, chunks: List[str]) -> Dict[str, float]:
        """
        Run all evaluation metrics on a set of chunks.
        """
        if len(chunks) < 2:
            return {
                'coherence': 1.0,
                'separation': 1.0,
                'size_variance': 0.0,
                'overall_score': 1.0
            }

        # Generate embeddings for each chunk
        embeddings = self.model.encode(chunks, convert_to_numpy=True)

        coherence = self.measure_coherence(chunks, embeddings)
        separation = self.measure_separation(embeddings)
        size_variance = self.measure_size_variance(chunks)

        # Weighted overall score
        overall = (coherence * 0.4) + (separation * 0.4) + ((1 - size_variance) * 0.2)

        return {
            'coherence': round(coherence, 3),
            'separation': round(separation, 3),
            'size_variance': round(size_variance, 3),
            'overall_score': round(overall, 3)
        }

    def measure_coherence(
        self,
        chunks: List[str],
        embeddings: np.ndarray
    ) -> float:
        """
        Measure how well sentences within each chunk relate to each other.
        Higher is better (sentences discuss same topic).
        """
        coherence_scores = []

        for i, chunk in enumerate(chunks):
            # Split chunk into sentences
            sentences = [s.strip() for s in chunk.split('.') if s.strip()]

            if len(sentences) < 2:
                coherence_scores.append(1.0)
                continue

            # Embed sentences within this chunk
            sent_embeddings = self.model.encode(sentences, convert_to_numpy=True)

            # Calculate pairwise similarities
            similarities = []
            for j in range(len(sent_embeddings)):
                for k in range(j + 1, len(sent_embeddings)):
                    sim = np.dot(sent_embeddings[j], sent_embeddings[k])
                    sim /= (np.linalg.norm(sent_embeddings[j]) * np.linalg.norm(sent_embeddings[k]))
                    similarities.append(sim)

            if similarities:
                coherence_scores.append(np.mean(similarities))
            else:
                coherence_scores.append(1.0)

        return np.mean(coherence_scores)

    def measure_separation(self, embeddings: np.ndarray) -> float:
        """
        Measure how distinct chunks are from each other.
        Higher is better (chunks cover different topics).

        We want low similarity between chunks, so we return 1 - avg_similarity.
        """
        if len(embeddings) < 2:
            return 1.0

        similarities = []
        for i in range(len(embeddings)):
            for j in range(i + 1, len(embeddings)):
                sim = np.dot(embeddings[i], embeddings[j])
                sim /= (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j]))
                similarities.append(sim)

        avg_similarity = np.mean(similarities)

        # Convert to separation score (lower similarity = higher separation)
        return 1 - avg_similarity

    def measure_size_variance(self, chunks: List[str]) -> float:
        """
        Measure how consistent chunk sizes are.
        Lower is better (uniform chunk sizes).

        Returns coefficient of variation (std/mean).
        """
        sizes = [len(chunk) for chunk in chunks]

        if len(sizes) < 2:
            return 0.0

        mean_size = np.mean(sizes)
        if mean_size == 0:
            return 0.0

        std_size = np.std(sizes)

        # Coefficient of variation, capped at 1
        return min(std_size / mean_size, 1.0)


# Example evaluation usage
def compare_chunking_methods(document: str):
    """
    Compare different chunking approaches on the same document.
    """
    from semantic_chunker import SemanticChunker
    from structural_chunker import StructuralChunker
    from hybrid_chunker import HybridChunker

    evaluator = ChunkEvaluator()

    methods = {
        'Fixed (500 chars)': lambda t: [t[i:i+500] for i in range(0, len(t), 500)],
        'Structural':        StructuralChunker().chunk,
        'Semantic':          SemanticChunker().chunk,
        'Hybrid':            HybridChunker().chunk,
    }

    results = {}
    for name, chunker in methods.items():
        chunks = chunker(document)
        metrics = evaluator.evaluate(chunks)
        metrics['num_chunks'] = len(chunks)
        metrics['avg_size'] = sum(len(c) for c in chunks) / len(chunks) if chunks else 0
        results[name] = metrics

    return results


if __name__ == '__main__':
    import argparse
    import random
    from pathlib import Path
    import sys

    parser = argparse.ArgumentParser(description='Evaluate semantic chunker quality')
    parser.add_argument(
        'file',
        nargs='?',
        default=None,
        help='Markdown file to evaluate (default: random file from sources/)',
    )
    args = parser.parse_args()

    if args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            sys.exit(1)
    else:
        all_files = sorted(Path('sources').rglob('*.md'), key=lambda f: f.stat().st_size, reverse=True)
        if not all_files:
            print("No .md files found under sources/", file=sys.stderr)
            sys.exit(1)
        path = random.choice(all_files[:10])

    # Use the pipeline preprocessor to get clean prose (same path as production)
    sys.path.insert(0, str(Path(__file__).parent))
    from pipeline import MarkdownPreprocessor

    raw_text = path.read_text(encoding='utf-8')
    sections = MarkdownPreprocessor().process(raw_text)
    document = ' '.join(prose for _, prose in sections if prose)

    if not document.strip() and not args.file:
        tried = {path}
        remaining = [f for f in all_files if f not in tried]
        for candidate in remaining:
            path = candidate
            raw_text = path.read_text(encoding='utf-8')
            sections = MarkdownPreprocessor().process(raw_text)
            document = ' '.join(prose for _, prose in sections if prose)
            if document.strip():
                break
        else:
            print("No prose content found in any source file.", file=sys.stderr)
            sys.exit(1)
    elif not document.strip():
        print("No prose content found after preprocessing.", file=sys.stderr)
        sys.exit(1)

    print(f"Evaluating: {path}")
    print(f"Document length: {len(document)} chars\n")

    results = compare_chunking_methods(document)

    col_w = max(len(k) for k in results) + 2
    metrics = ['num_chunks', 'avg_size', 'coherence', 'separation', 'size_variance', 'overall_score']

    header = f"{'Method':<{col_w}}" + ''.join(f"{m:>16}" for m in metrics)
    print(header)
    print('-' * len(header))

    for method, scores in results.items():
        row = f"{method:<{col_w}}"
        for m in metrics:
            val = scores.get(m, 0)
            row += f"{val:>16}" if isinstance(val, int) else f"{val:>16.3f}"
        print(row)