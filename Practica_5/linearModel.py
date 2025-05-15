import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("cleaned_steam.csv").sample(n=1000, random_state=42)

df = df.dropna(subset=["price", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max", "release_date"])

df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year
df["release_days"] = (df["release_date"] - df["release_date"].min()).dt.days

correlation_matrix = df[["price", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max", "release_days"]].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.title("Feature Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

X = df[["release_days", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max"]]
y = df["price"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"Linear Model R² Score: {r2:.3f}")

plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label="Actual Price", marker="o", linestyle="")
plt.plot(y_pred, label="Predicted Price", marker="x", linestyle="dashed", color="red")
plt.xlabel("Game Index")
plt.ylabel("Price ($)")
plt.legend()
plt.title("Linear Regression: Actual vs. Predicted Prices Over Time")
plt.grid(True)
plt.savefig("linear_regression_predictions.png")
plt.show()