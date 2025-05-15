import pandas as pd
import matplotlib.pyplot as plt

df_genres = pd.read_csv("genres_normalized.csv")

genre_counts = df_genres["genres"].value_counts()

plt.figure(figsize=(12, 6))
genre_counts.plot(kind="bar", color="skyblue")
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.title("Top Game Genres by Count")
plt.xticks(rotation=90) 
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.subplots_adjust(bottom=0.35)

plt.savefig("genre_bar_chart.png", dpi=300)
plt.show()