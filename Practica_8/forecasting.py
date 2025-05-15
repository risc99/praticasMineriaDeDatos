import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("cleaned_steam.csv").dropna(subset=["release_date", "price"])

df = df[df["price"] <= 100]

df["release_date"] = pd.to_datetime(df["release_date"])

df["release_days"] = (df["release_date"] - df["release_date"].min()).dt.days

X = df[["release_days"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def polynomial_features(X, degree=2):
    return [[x[0]**i for i in range(degree + 1)] for x in X.values]

X_train_poly = polynomial_features(X_train, degree=2)
X_test_poly = polynomial_features(X_test, degree=2)

model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

future_days = [[df["release_days"].max() + i] for i in range(365)]
future_days_poly = polynomial_features(pd.DataFrame(future_days), degree=2)
future_prices = model_poly.predict(future_days_poly)

plt.figure(figsize=(10, 6))
plt.scatter(df["release_days"], df["price"], label="Actual Prices", alpha=0.5)
plt.plot([x[0] for x in future_days], future_prices, label="Polynomial Predicted Prices", color="blue", linewidth=2)
plt.xlabel("Days Since First Release")
plt.ylabel("Price ($)")
plt.title("Steam Game Price Forecast (Polynomial Regression, No Extra Libraries)")
plt.legend()
plt.grid(True)
plt.savefig("price_forecast_poly_no_libs.png")
plt.show()