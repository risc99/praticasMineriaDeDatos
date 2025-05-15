import pandas as pd
import matplotlib.pyplot as plt

df_devs = pd.read_csv("developer_normalized.csv")

devs_counts = df_devs["developer"].value_counts()

plt.rcParams["font.family"] = "Arial"
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(20, 8))
devs_counts[:20].plot(kind="bar", color="skyblue")
plt.xlabel("Developer")
plt.ylabel("Number of Games")
plt.title("Top 20 Game Developers by Count")
plt.xticks(rotation=90, fontsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.subplots_adjust(bottom=0.3)

plt.savefig("bar_chart_developer.png", dpi=300)
plt.show()