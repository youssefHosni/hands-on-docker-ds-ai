import os

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel, Field

from rag import COLLECTION, embed_question, qdrant

# Set by Compose, like the embedding model's variables
LLM_MODEL = os.environ["LLM_MODEL"]
llm = OpenAI(base_url=os.environ["LLM_URL"], api_key="unused")

PROMPT = """Answer the question using only the context below. First quote the sentence from the
context that answers it, then answer in one sentence. If the context doesn't contain the answer,
say "I don't know".

Context:
{context}

Question: {question}"""

app = FastAPI()


class Question(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    top_k: int = Field(default=3, ge=1, le=10)


@app.get("/health")
def health():
    return {"status": "ok", "chunks": qdrant.count(COLLECTION).count}


@app.post("/ask")
def ask(q: Question):
    # 1. Retrieve: the chunks closest in meaning to the question
    hits = qdrant.query_points(COLLECTION, query=embed_question(q.question), limit=q.top_k).points
    context = "\n\n".join(f"{h.payload['section']}: {h.payload['text']}" for h in hits)

    # 2. Generate: the LLM answers from those chunks only
    reply = llm.chat.completions.create(
        model=LLM_MODEL,
        temperature=0,
        messages=[{"role": "user", "content": PROMPT.format(context=context, question=q.question)}],
    )
    return {
        "answer": reply.choices[0].message.content.strip(),
        "sources": [
            {"file": h.payload["file"], "section": h.payload["section"], "score": round(h.score, 3)}
            for h in hits
        ],
    }
