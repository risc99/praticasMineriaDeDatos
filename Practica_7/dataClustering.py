import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("cleaned_steam.csv").sample(n=1000, random_state=42)

features = ["price", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max"]
df_cluster = df[features].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

k = 5
kmeans = KMeans(n_clusters=k, random_state=42)

df_cluster["cluster"] = kmeans.fit_predict(X_scaled)

print(df_cluster.head())

df_cluster = df_cluster.reset_index(drop=True)
df["cluster"] = df_cluster["cluster"].values

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["positive_ratings"], y=df["price"], hue=df["cluster"], palette="viridis")
plt.xlabel("Positive Ratings")
plt.ylabel("Price ($)")
plt.title("K-Means Clustering of Steam Games")
plt.legend(title="Cluster")
plt.grid(True)
sns.pairplot(df_cluster, hue="cluster", palette="viridis")
plt.savefig("kmeans_pairplot.png")
plt.show()