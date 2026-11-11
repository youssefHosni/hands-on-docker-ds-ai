# Chapter 5 exercise: answer

`Dockerfile` in this folder is `ch05/multi-stage/Dockerfile` with one change in the final stage:

```dockerfile
# The API doesn't need pip: remove it, with the packages it carries inside
RUN pip uninstall --yes --root-user-action=ignore pip && useradd --create-home appuser
```

(`--root-user-action=ignore` only silences pip's warning about running as root, which is fine in a
build step.) Run 1 Nov 2026, recorded in `outputs/ch05-exercise.txt`:

```
$ docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v trivy-cache:/root/.cache aquasec/trivy:0.76.1 image --quiet --severity HIGH,CRITICAL ml-app:3.0-nopip | grep -E "^Total|^ml-app|^Python"
ml-app:3.0-nopip (debian 13.7)
Total: 46 (HIGH: 46, CRITICAL: 0)

$ docker images ml-app:3.0*
IMAGE               ID             DISK USAGE   CONTENT SIZE   EXTRA
ml-app:3.0          a4a18bcb63a8        605MB          130MB
ml-app:3.0-nopip    417da254f57a        612MB          132MB
```

- **Python findings left: none.** The Python section is gone from the report: the vulnerable
  `msgpack`, `setuptools` and `urllib3` copies were inside pip. The 46 Debian findings stay; they come
  from the base image.
- **Size: 7 MB *bigger*.** pip's files are still stored in the base image's layers. Uninstalling it in
  a later layer only hides them, and the new layer records what was removed. That's the lesson of
  "Fewer, Smarter Layers": deleting a file later never makes an image smaller.
- The API still works: `{"prediction":[12.000000000000002]}` for an input of 6.

To make the image smaller *and* pip-free, the final stage would need a base image without pip,
like a Docker Hardened Image for Python.
