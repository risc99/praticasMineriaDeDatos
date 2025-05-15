import pandas as pd

# Ricardo Issac Sánchez Clark, Minería de datos 035

# This should load the dataset
df = pd.read_csv("cleaned_steam.csv")

# This should check if there is any empty values in the dataset count it and print the number of missing values by columns
print(df.isnull().sum())

# This should count all 'Unknown' data
unknown_counts = (df == "Unknown").sum()
print(unknown_counts)
# There is a dev missing and 14 publishers
# There is also a game, but that's probably the actual name of the game