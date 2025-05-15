import pandas as pd
from scipy.stats import f_oneway, ttest_ind, kruskal

df = pd.read_csv("cleaned_steam.csv")
df["genres"] = df["genres"].str.split(",")
df = df.explode("genres")

columns_to_test = ["price", "positive_ratings", "negative_ratings", "average_playtime"]
categorical_column = "genres"

valid_groups = [group for group in df[categorical_column].unique() if df[df[categorical_column] == group].shape[0] > 1]

anova_results = {col: f_oneway(*[df[df[categorical_column] == group][col].dropna() for group in valid_groups]) 
                 for col in columns_to_test}

print("ANOVA Results:")
for col, result in anova_results.items():
    print(f"{col}: F={result.statistic:.3f}, p={result.pvalue:.3f}")

unique_genres = df["genres"].unique()

if len(unique_genres) >= 2:  # Ensure there are at least two genres
    genre1 = unique_genres[0]
    genre2 = unique_genres[1]

    group1 = df[df["genres"] == genre1]["price"].dropna()
    group2 = df[df["genres"] == genre2]["price"].dropna()

    t_test_result = ttest_ind(group1, group2)
    
    print(f"\nT-Test Result for Price between {genre1} vs {genre2}: t={t_test_result.statistic:.3f}, p={t_test_result.pvalue:.3f}")
else:
    print("Error: Not enough unique genres for a T-Test.")

kruskal_results = {col: kruskal(*[df[df[categorical_column] == group][col].dropna() for group in valid_groups]) 
                   for col in columns_to_test}

print("\nKruskal-Wallis Test Results:")
for col, result in kruskal_results.items():
    print(f"{col}: H={result.statistic:.3f}, p={result.pvalue:.3f}")