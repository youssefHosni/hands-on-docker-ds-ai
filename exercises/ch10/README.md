# Chapter 10 exercise: Open WebUI with Docker Model Runner

Task: keep the chapter's Compose stack as it is, and add an override file that makes Open WebUI
also list the model you pulled with Docker Model Runner.

Answer: `compose.dmr.yaml`. Open WebUI talks to any OpenAI-compatible server through
`OPENAI_API_BASE_URL`, and Model Runner's OpenAI-compatible API lives under `/engines/v1`.

```bash
docker compose -f compose.yaml -f compose.dmr.yaml --profile ui up -d
docker compose exec open-webui curl -s http://model-runner.docker.internal:12434/engines/v1/models
```

The model list in Open WebUI now shows `docker.io/ai/gemma3:1B-Q4_K_M` next to `gemma3:1b`
(`open-webui-dmr.png`, recorded run in `outputs/ch10-exercise.txt`).

- On Docker Engine (Linux), Model Runner listens on port 12434 of the host. `host-gateway` makes the
  host reachable from the container under the name `model-runner.docker.internal`.
- On Docker Desktop, containers reach Model Runner at `http://model-runner.docker.internal/engines/v1`
  without `extra_hosts` (Docker's documentation; not run here).
- `OPENAI_API_KEY` can be anything: Model Runner ignores it.
