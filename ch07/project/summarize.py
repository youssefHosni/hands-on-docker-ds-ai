import sys
from pathlib import Path

import pandas as pd

# Usage: python summarize.py <input.csv> <output.csv>
source, target = sys.argv[1], Path(sys.argv[2])

houses = pd.read_csv(source)
summary = houses.describe().round(1)
target.parent.mkdir(parents=True, exist_ok=True)
summary.to_csv(target)
print(summary)
