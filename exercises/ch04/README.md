# Chapter 4 exercise: answer

`Dockerfile` in this folder is Chapter 3's, with a regular user and a health check. The other files
are copied from `ch03/`. Run 1 Nov 2026, recorded in `outputs/ch04-exercise.txt`.

The changes:

```dockerfile
RUN useradd --create-home appuser          # near the top, so it's cached
...
RUN python train.py
USER appuser                               # after the build steps that need root
...
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')"
```

Checking it:

```
$ docker exec ml-ex whoami
appuser
$ docker ps --filter name=ml-ex --format "table {{.Names}}\t{{.Status}}"
NAMES     STATUS
ml-ex     Up 13 seconds (healthy)
```

Two things to watch:

- `USER appuser` must come **after** `RUN pip install` and `RUN python train.py`. Before them, those
  steps would run as `appuser`, which can't write to the system Python's folders.
- The `/` route answers even if the model failed to load, so this check only proves the server is up.
  Chapter 4's `/health` route (in `ch04/app/app.py`) also checks the model.
