import mlflow

# The tracking server, by its container name on the Docker network
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("iris")

# Log one run: a parameter and a metric
with mlflow.start_run():
    mlflow.log_param("C", 1.0)
    mlflow.log_metric("accuracy", 0.9733)

# Read the runs back from the server
runs = mlflow.search_runs(experiment_names=["iris"])
print(runs[["params.C", "metrics.accuracy", "status"]])
