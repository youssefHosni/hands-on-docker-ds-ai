# Chapter 11 exercise: a load test that runs in Compose

**Task.** Run `load.py` from a container instead of from your machine: add a `load` service to the
server's Compose file that waits until the server is healthy, calls it by its service name, and only
starts when you ask for it.

**Answer.** `compose.yaml` here builds the server from `ch11/server` and adds a `load` service under the
`load` profile (`load/Dockerfile` + a copy of `ch11/load/load.py`). The arguments are in `command`, so
they can be changed on the command line.

```bash
docker compose --profile load run --rm load
docker compose --profile load run --rm load http://server:8000/predict 1 20
docker compose down
```

The server is reached as `http://server:8000`, not `localhost` (Chapter 10), and `depends_on` with
`condition: service_healthy` uses the HEALTHCHECK from the server's Dockerfile, so the test never
starts before the model is loaded. Recorded run: `outputs/ch11-exercise.txt`.
