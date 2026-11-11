CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE movies (id serial PRIMARY KEY, title text, embedding vector(3));
INSERT INTO movies (title, embedding) VALUES
  ('Alien', '[0.9, 0.1, 0.0]'),
  ('Notting Hill', '[0.1, 0.9, 0.0]'),
  ('The Thing', '[0.8, 0.2, 0.1]'),
  ('Love Actually', '[0.2, 0.8, 0.1]');
-- the two movies closest to a "romance" query, by cosine distance
SELECT title, embedding <=> '[0.0, 1.0, 0.0]' AS distance
FROM movies ORDER BY distance LIMIT 2;
