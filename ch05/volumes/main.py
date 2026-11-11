import csv
import os
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# The experiment's setting, from an environment variable
C = float(os.environ.get("C", "1.0"))

# Run the experiment
X, y = load_iris(return_X_y=True)
accuracy = cross_val_score(LogisticRegression(C=C, max_iter=1000), X, y, cv=5).mean()

# Append the result to data/results.csv
results = Path("data/results.csv")
new_file = not results.exists()
with results.open("a", newline="") as f:
    writer = csv.writer(f)
    if new_file:
        writer.writerow(["C", "accuracy"])
    writer.writerow([C, round(accuracy, 4)])

print(results.read_text())
