# Chapter 6 exercise: answer

`movies.sql` in this folder is `ch06/11-pgvector/movies.sql` with a fourth movie, Love Actually
(`[0.2, 0.8, 0.1]`), and a "romance" query, `[0.0, 1.0, 0.0]`. In Qdrant, the same movie is the fourth
point of the upsert. Run 1 Nov 2026, recorded in `outputs/ch06-exercise.txt`:

```
$ curl -s -X POST http://localhost:6333/collections/movies/points/query -H 'Content-Type: application/json' -d '{"query": [0.0, 1.0, 0.0], "limit": 2, "with_payload": true}'
{"result":{"points":[{"id":2,"version":1,"score":0.9938837,"payload":{"title":"Notting Hill"}},{"id":4,"version":1,"score":0.9630868,"payload":{"title":"Love Actually"}}]},"status":"ok","time":0.000591293}

$ docker exec -i pgvector psql -U postgres < movies.sql
...
     title     |       distance
---------------+----------------------
 Notting Hill  | 0.006116251198662548
 Love Actually |  0.03691315929883732
(2 rows)
```

- **Same movies, same order.** Both databases return Notting Hill first and Love Actually second.
- **Why the numbers look so different:** Qdrant's `score` is the cosine *similarity* (1 means the same
  direction, so higher is closer). pgvector's `<=>` operator is the cosine *distance*, which is
  1 − similarity (0 means the same direction, so lower is closer). 1 − 0.9938837 = 0.0061163: the same
  number, seen from the other side. That's why the SQL sorts with `ORDER BY distance` (smallest first).
- The numbers also match the chapter's "Alien" query: Notting Hill is to `[0, 1, 0]` what Alien is to
  `[1, 0, 0]`, so the scores are identical.
