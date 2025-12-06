# custodian_heatmap.py
# One-click custodian vs date volume heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data/custodians_sample.csv", parse_dates=["Date"])

# Create pivot
pivot = df.pivot_table(index="Custodian", columns=df["Date"].dt.date, values="DocCount", aggfunc="sum", fill_value=0)

plt.figure(figsize=(14, 8))
sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd", linewidths=.5)
plt.title("Document Volume Heatmap by Custodian & Date", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Custodian")
plt.tight_layout()
plt.savefig("sample_data/custodian_heatmap_python.png", dpi=300)
plt.show()
print("Heatmap saved as custodian_heatmap_python.png")
