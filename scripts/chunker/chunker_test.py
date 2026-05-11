
from semantic_chunker import SemanticChunker

## Open document and read content
with open("sources/personal/tips_svenskan_mcmc.md", "r", encoding="utf-8") as f:
    document = f.read()

# Initialize chunker with tuned parameters
chunker = SemanticChunker(
    similarity_threshold=0.2,  # Adjust based on your content
    min_chunk_size=100,
    max_chunk_size=1500
)

chunks = chunker.chunk(document)

print(f"Document split into {len(chunks)} semantic chunks:\n")
for i, chunk in enumerate(chunks, 1):
    print(f"--- Chunk {i} ({len(chunk)} chars) ---")
    print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
    print()