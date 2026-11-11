# Read the database password from the Compose secret and start the MLflow server.
# The address goes in an environment variable, not on the command line, where `docker top` would show it.
# exec replaces the shell with MLflow, so MLflow receives docker stop's signal.
export MLFLOW_BACKEND_STORE_URI="postgresql://mlflow:$(cat /run/secrets/db_password)@db:5432/mlflow"
exec mlflow server --host 0.0.0.0 --port 5000 \
    --artifacts-destination /mlartifacts \
    --allowed-hosts mlflow:5000,localhost:5001
