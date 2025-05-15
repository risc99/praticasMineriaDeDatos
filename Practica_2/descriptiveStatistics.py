import pandas as pd

df = pd.read_csv("cleaned_steam.csv")
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
# This gave me nightmares, I didn't understand why I saved release_date as type datetime and here it was type object
# It seems like pandas changes datetime to object when it reads the csv and I have to change it again
# It's very stupid
#Then it took me days for me to figure why my charts where a cluster of nodes, so I had to change them to bar graphs
df_Categories = pd.read_csv("categories_normalized.csv")
df_Devs = pd.read_csv("developer_normalized.csv")
df_Genres = pd.read_csv("genres_normalized.csv")
df_Platforms = pd.read_csv("platforms_normalized.csv")
df_Publishers = pd.read_csv("publisher_normalized.csv")
df_Tags = pd.read_csv("steamspy_tags_normalized.csv")

df_genresP = df_Genres.merge(df[["appid", "price"]], on="appid", how="left")
df_categoriesP = df_Categories.merge(df[["appid", "price"]], on="appid", how="left")
df_developersP = df_Devs.merge(df[["appid", "price"]], on="appid", how="left")
df_publishersP = df_Publishers.merge(df[["appid", "price"]], on="appid", how="left")
df_platformsP = df_Platforms.merge(df[["appid", "price"]], on="appid", how="left")
df_tagsP = df_Tags.merge(df[["appid", "price"]], on="appid", how="left")

df_genresAP = df_Genres.merge(df[["appid", "average_playtime"]], on="appid", how="left")
df_categoriesAP = df_Categories.merge(df[["appid", "average_playtime"]], on="appid", how="left")
df_developersAP = df_Devs.merge(df[["appid", "average_playtime"]], on="appid", how="left")
df_publishersAP = df_Publishers.merge(df[["appid", "average_playtime"]], on="appid", how="left")
df_platformsAP = df_Platforms.merge(df[["appid", "average_playtime"]], on="appid", how="left")
df_tagsAP = df_Tags.merge(df[["appid", "average_playtime"]], on="appid", how="left")

print(df.info())  

for i in range(10):
    print("--")

print("Average Price:", df["price"].mean())
print("Median Price:", df["price"].median())

for i in range(10):
    print("--")

print("Most Common Genre:", df_Genres["genres"].mode()[0])
print("Most Common Category:", df_Categories["categories"].mode()[0])
print("Most Common Tag:", df_Tags["steamspy_tags"].mode()[0])
print("Most Common Developer:", df_Devs["developer"].mode()[0])
print("Most Common Publisher:", df_Publishers["publisher"].mode()[0])

for i in range(10):
    print("--")

top_genres = df_genresP.groupby("genres")["price"].mean().sort_values(ascending=False)
top_categories = df_categoriesP.groupby("categories")["price"].mean().sort_values(ascending=False)
top_developers = df_developersP.groupby("developer")["price"].mean().sort_values(ascending=False)
top_publishers = df_publishersP.groupby("publisher")["price"].mean().sort_values(ascending=False)

print("\nTop Expensive Genres:\n", top_genres.head(10))
print("\nTop Expensive Categories:\n", top_categories.head(10))
print("\nTop Expensive Developers:\n", top_developers.head(10))
print("\nTop Expensive Publishers:\n", top_publishers.head(10))

print("\nAverage price by date:\n", df.groupby("release_date")["price"].mean().head())
print("\nAverage playtime by date:\n", df.groupby("release_date")["average_playtime"].mean().head())

for i in range(10):
    print("--")

top_played_genres = df_genresAP.groupby("genres")["average_playtime"].mean().sort_values(ascending=False).head(10)
top_played_categories = df_categoriesAP.groupby("categories")["average_playtime"].mean().sort_values(ascending=False).head(10)
top_played_developers = df_developersAP.groupby("developer")["average_playtime"].mean().sort_values(ascending=False).head(10)
top_played_publishers = df_publishersAP.groupby("publisher")["average_playtime"].mean().sort_values(ascending=False).head(10)

print("\nMost Played Genres:\n", top_played_genres)
print("\nMost Played Categories:\n", top_played_categories)
print("\nMost Played Developers:\n", top_played_developers)
print("\nMost Played Publishers:\n", top_played_publishers)