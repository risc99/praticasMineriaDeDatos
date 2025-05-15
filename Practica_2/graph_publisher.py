import pandas as pd
import matplotlib.pyplot as plt

df_pub = pd.read_csv("publisher_normalized.csv")

pub_counts = df_pub["publisher"].value_counts()

plt.rcParams["font.family"] = "Arial"
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(20, 8))
pub_counts[:20].plot(kind="bar", color="skyblue")
plt.xlabel("Pblisher")
plt.ylabel("Number of Games")
plt.title("Top 20 Game Publishers by Count")
plt.xticks(rotation=90, fontsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.subplots_adjust(bottom=0.3)

plt.savefig("bar_chart_publisher.png", dpi=300)
plt.show()