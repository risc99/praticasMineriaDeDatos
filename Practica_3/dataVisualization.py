import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_steam.csv")

df["release_date"] = pd.to_datetime(df["release_date"])
df["release_year"] = df["release_date"].dt.year

columns_to_plot = ["price", "positive_ratings", "negative_ratings", "average_playtime", "owners_min", "owners_max", "release_year"]
plot_types = ["hist", "boxplot", "scatter", "bar"]

for col in columns_to_plot:
    for plot in plot_types:
        plt.figure(figsize=(10, 6))
        
        if plot == "hist":
            df[col].hist(bins=30, color="skyblue", edgecolor="black")
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")

        elif plot == "boxplot":
            sns.boxplot(y=df[col])
            plt.title(f"Boxplot of {col}")

        elif plot == "scatter":
            sns.scatterplot(x=df[col], y=df["positive_ratings"])  
            plt.title(f"Scatter Plot: {col} vs. Positive Ratings")
            plt.xlabel(col)
            plt.ylabel("Positive Ratings")

        elif plot == "bar":
            if df[col].nunique() < 50:
                df[col].value_counts().head(20).plot(kind="bar", color="skyblue")
                plt.title(f"Bar Chart of {col}")
                plt.xticks(rotation=90)

        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.savefig(f"{col}_{plot}.png")
        plt.close()