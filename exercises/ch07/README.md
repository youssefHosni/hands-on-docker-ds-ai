# Chapter 7 exercise: answer

`devcontainer.json` in this folder is `ch07/project/.devcontainer/devcontainer.json` with two more
settings:

```jsonc
  "mounts": ["source=datasets,target=/datasets,type=volume"],
  "containerEnv": {"SCIKIT_LEARN_DATA": "/datasets"},
```

- **`mounts`** adds the `datasets` named volume at `/datasets`, the folder the Dockerfile created for
  `appuser`. The project itself is still the `workspaceMount` bind mount.
- **`containerEnv`** sets `SCIKIT_LEARN_DATA` for every process in the container, so the code doesn't need
  `data_home=` and the `-e` flag isn't needed either.

Copy it over `ch07/project/.devcontainer/devcontainer.json` and rebuild the dev container (in VS Code:
**Dev Containers: Rebuild Container**; or with the CLI as below). Run 2 Nov 2026 with Dev Containers CLI
0.90.0, recorded in `outputs/ch07-exercise.txt`:

```
$ devcontainer up --workspace-folder .
...
$ devcontainer exec --workspace-folder . ls -l /datasets
total 360
-rw-r--r-- 1 appuser appuser 366871 Nov  1 22:18 cal_housing_py3.pkz

$ devcontainer exec --workspace-folder . python -c "from sklearn.datasets import fetch_california_housing; print(fetch_california_housing().data.shape)"
(20640, 8)
```

The file's date is from the earlier `docker run` that downloaded it: the dev container found the dataset
in the volume and didn't download it again. Rebuild the dev container as often as you like; the volume
stays until you run `docker volume rm datasets`.
