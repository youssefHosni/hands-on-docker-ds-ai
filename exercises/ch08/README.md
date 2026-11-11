# Chapter 8 exercise: answer

The second training run (`C=0.01`) became version 2 and the champion, with a lower accuracy (0.8222
against 1.0000 for version 1). To serve version 1 again, point the `champion` alias back at it, with a
one-off container of the `trainer` service (its image has the MLflow client, and Compose gives it
`MLFLOW_TRACKING_URI`), then restart the API, which loads the champion when it starts.

Run 2 Nov 2026 in `ch08/project/`, recorded in `outputs/ch08-exercise.txt`:

```
$ docker compose run --rm -e C=0.01 trainer
...
C=0.01, accuracy=0.8222: iris version 2 is now the champion

$ docker compose restart api
$ curl -s http://localhost:8000/health
{"status":"ok","model_version":"2"}

$ docker compose run --rm trainer python -c "from mlflow import MlflowClient; MlflowClient().set_registered_model_alias('iris', 'champion', '1')"
...
$ docker compose restart api
$ curl -s http://localhost:8000/health
{"status":"ok","model_version":"1"}
```

- **`docker compose run --rm trainer <command>`** replaces the service's `CMD` (`python train.py`) with
  your command, but keeps everything else from the Compose file: the image, the environment and the
  network, so `http://mlflow:5000` works.
- Nothing was retrained or rebuilt: the alias is the only thing that changed. That's why serving
  "whatever the alias points to" is handy: rolling back is one command and a restart.
- You can do the same in the MLflow interface (`http://localhost:5001`, Models, iris, version 1, add
  the alias), which is what most teams do.
