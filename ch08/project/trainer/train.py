import os

import mlflow
from mlflow import MlflowClient
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# MLFLOW_TRACKING_URI comes from the Compose file
mlflow.set_experiment("iris")

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

C = float(os.environ.get("C", "1.0"))
with mlflow.start_run():
    model = LogisticRegression(C=C, max_iter=500).fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    mlflow.log_param("C", C)
    mlflow.log_metric("accuracy", accuracy)
    # Save the model in MLflow and register it as a new version of the "iris" model
    info = mlflow.sklearn.log_model(model, name="model", registered_model_name="iris")

# The API serves whichever version the "champion" alias points to
version = info.registered_model_version
MlflowClient().set_registered_model_alias("iris", "champion", version)
print(f"C={C}, accuracy={accuracy:.4f}: iris version {version} is now the champion")
