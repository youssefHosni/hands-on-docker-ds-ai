import os

from openai import OpenAI
from qdrant_client import QdrantClient

# Compose sets these two from the models: section of compose.yaml
EMBEDDING_URL = os.environ["EMBEDDING_URL"]
EMBEDDING_MODEL = os.environ["EMBEDDING_MODEL"]

QDRANT_URL = os.environ.get("QDRANT_URL", "http://qdrant:6333")
COLLECTION = "handbook"

# Docker Model Runner speaks the OpenAI API and needs no key
embedder = OpenAI(base_url=EMBEDDING_URL, api_key="unused")
qdrant = QdrantClient(url=QDRANT_URL)


def embed(texts: list[str]) -> list[list[float]]:
    response = embedder.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


# EmbeddingGemma expects these prefixes on documents and on questions
def embed_documents(chunks: list[dict]) -> list[list[float]]:
    return embed([f"title: {c['section']} | text: {c['text']}" for c in chunks])


def embed_question(question: str) -> list[float]:
    return embed([f"task: search result | query: {question}"])[0]
