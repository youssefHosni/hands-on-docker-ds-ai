import mlflow

# The tracking server, by its service name on the Compose network
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("iris")

# Log one run: a parameter, a metric and a small file (an artifact)
with mlflow.start_run():
    mlflow.log_param("C", 1.0)
    mlflow.log_metric("accuracy", 0.9733)
    mlflow.log_text("Trained on the iris dataset.", "notes.txt")

runs = mlflow.search_runs(experiment_names=["iris"])
print(runs[["params.C", "metrics.accuracy", "status"]])
