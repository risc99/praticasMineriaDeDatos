import pandas as pd

# Ricardo Issac Sánchez Clark
# Now I want to make a csv for each normalized column

df = pd.read_csv("normalized_steam.csv")

columns_to_split = ["developer", "publisher", "platforms", "categories", "genres", "steamspy_tags","release_date"]

for column in columns_to_split:
    output_df = df[["appid", column]].drop_duplicates()
    output_df.to_csv(f"{column}_normalized.csv", index=False)
    print(f"Saved {column}_normalized.csv!")

print("All files have been successfully created.")