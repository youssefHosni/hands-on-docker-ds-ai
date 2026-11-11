# Chapter 9 exercise: answer

`compose.yaml` in this folder builds `ch09/pytorch/Dockerfile` (copied here with `check_gpu.py`) twice,
with a different `TORCH_INDEX` build argument, and puts each build in its own profile:

- **`check-cpu`** (profile `cpu`): `build.args` sets `TORCH_INDEX` to PyTorch's CPU index. Small image,
  runs anywhere.
- **`check-gpu`** (profile `gpu`): the default build (PyPI, with CUDA 13.2), and a GPU reservation for all
  GPUs.
- `image:` names each build, so the two don't overwrite each other.

Run 2 Nov 2026 on a Mac (Apple Silicon, no NVIDIA GPU), recorded in `outputs/ch09-exercise.txt`:

```
$ docker compose --profile cpu up --build
...
check-cpu-1  | PyTorch: 2.15.0+cpu
check-cpu-1  | Built for CUDA: None
check-cpu-1  | NVIDIA GPU available: False
check-cpu-1  | Apple GPU (MPS) available: False
```

The `gpu` profile can't run here, but `docker compose --profile gpu config` shows what Compose will ask
Docker for:

```
    deploy:
      resources:
        reservations:
          devices:
            - capabilities:
                - gpu
              driver: nvidia
              count: -1
```

`count: -1` is how Compose writes `all`. On a Linux machine with an NVIDIA GPU and the Container
Toolkit, `docker compose --profile gpu up --build` prints `NVIDIA GPU available: True` and the GPU's name
(not run for the book: no GPU machine).
