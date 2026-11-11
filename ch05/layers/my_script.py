import pandas as pd
import matplotlib
matplotlib.use("Agg")  # no screen in a container: draw to a file
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
sales = pd.read_csv("data/sales.csv")

# Summarize it
print(sales.groupby("region")["revenue"].sum())

# Plot it
sns.barplot(data=sales, x="month", y="revenue", hue="region")
plt.savefig("sales.png")
print("Plot saved to sales.png")
