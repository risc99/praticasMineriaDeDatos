import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("cleaned_steam.csv").sample(n=1000, random_state=42)

df = df.dropna(subset=["price", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max", "genres"])

genre_mapping = {
    "Action": "Action",
    "Adventure": "Adventure",
    "RPG": "RPG",
    "Simulation": "Simulation",
    "Sports": "Sports",
    "Strategy": "Strategy",
    "Shooter": "Shooter",
    "Casual": "Casual",
    "Racing": "Racing"
}
df["general_genre"] = df["genres"].map(lambda x: genre_mapping.get(x, "Other"))

label_encoder = LabelEncoder()
df["genre_encoded"] = label_encoder.fit_transform(df["general_genre"])

balanced_df = df.groupby("genre_encoded").apply(lambda x: x.sample(n=min(len(x), 100), random_state=42))
balanced_df = balanced_df.reset_index(drop=True)

X = balanced_df[["positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max"]]
y = balanced_df["genre_encoded"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

unique_classes = sorted(set(y_test) | set(y_pred))
target_names = label_encoder.inverse_transform(unique_classes)

accuracy = accuracy_score(y_test, y_pred)
print(f"KNN Classification Accuracy: {accuracy:.3f}")

print("Classification Report:")
print(classification_report(y_test, y_pred, labels=unique_classes, target_names=target_names, zero_division=1))