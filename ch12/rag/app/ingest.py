import os
import time
from pathlib import Path

from qdrant_client.models import Distance, PointStruct, VectorParams

from rag import COLLECTION, embed_documents, qdrant

DOCS_DIR = Path(os.environ.get("DOCS_DIR", "/docs"))


def split(path: Path) -> list[dict]:
    """One chunk per '## ' section of a Markdown file."""
    chunks = []
    for part in path.read_text().split("\n## ")[1:]:
        section, _, text = part.partition("\n")
        chunks.append({"file": path.name, "section": section, "text": " ".join(text.split())})
    return chunks


start = time.perf_counter()
files = sorted(DOCS_DIR.glob("*.md"))
chunks = [chunk for path in files for chunk in split(path)]
vectors = embed_documents(chunks)

# Start from an empty collection, so deleted or changed files leave nothing behind
if qdrant.collection_exists(COLLECTION):
    qdrant.delete_collection(COLLECTION)
qdrant.create_collection(
    COLLECTION, vectors_config=VectorParams(size=len(vectors[0]), distance=Distance.COSINE)
)
qdrant.upsert(
    COLLECTION,
    points=[PointStruct(id=i, vector=v, payload=c) for i, (v, c) in enumerate(zip(vectors, chunks))],
)
seconds = time.perf_counter() - start
print(f"Ingested {len(chunks)} chunks from {len(files)} files "
      f"({len(vectors[0])} dimensions) in {seconds:.1f} s")
