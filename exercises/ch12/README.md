# Chapter 12 exercise: a new document, without restarting the API

**Task.** Add a new document to the RAG project, read it into Qdrant without restarting the API, and ask
a question that only the new document can answer.

**Answer.** `security.md` here is a small document about laptop security. From `ch12/rag`:

```bash
cp ../../exercises/ch12/security.md docs/
docker compose run --rm ingest
curl -s localhost:8000/ask -H "Content-Type: application/json" \
  -d '{"question": "I lost my laptop on Saturday. Can I wait until Monday to report it?"}'
```

`ingest` reports 21 chunks from 7 files instead of 18 from 6, and the answer comes from `security.md`:
report it within 2 hours, even outside working hours. The API didn't restart: it asks Qdrant on every
request, and the new collection is there.

To go back, delete the file and run `docker compose run --rm ingest` again. Because `ingest` starts from an
empty collection, the deleted document leaves nothing behind (18 chunks from 6 files again).
Recorded run: `outputs/ch12-exercise.txt`.
