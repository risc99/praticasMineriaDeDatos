import pandas as pd

# Ricardo Issac Sánchez Clark, Minería de datos 035
# I'm pretty sure this dataset has been used before, it is humongous, Thank you Rainbow CVS :'(
# If there is something unclear in the code comments, I apologize, I'm not used to doing it, sadly
# At least it's easier than trying to comment the code in my games, that's a nightmare

# This should load the dataset
df = pd.read_csv("steam_dataset/steam.csv")

# This should check if there is any empty values in the dataset count it and print the number of missing values by columns
print(df.isnull().sum())
# The print shows there is a developer missing and 14 publishers.

#This should fill any missing values with 'Unknown'
df["name"].fillna("Unknown", inplace=True)
df["developer"].fillna("Unknown", inplace=True)
df["publisher"].fillna("Unknown", inplace=True)
df["platforms"].fillna("Unknown", inplace=True)
df["categories"].fillna("Unknown", inplace=True)
df["genres"].fillna("Unknown", inplace=True)
df["steamspy_tags"].fillna("Unknown", inplace=True)

# If there are any missing prices, this should set the median as it's value
df["price"].fillna(df["price"].median(), inplace=True)
#In this case there was none, since the print showed no missing values

# This one should convert the dates in release_date to type datetime
df["release_date"] = df["release_date"].astype(str)  # Convert to string first
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
##The date format was already correct in the original file

# Split owners into to columns and convert them to int
df[["owners_min", "owners_max"]] = df["owners"].str.split("-", expand=True).astype(int)
df.drop(columns=["owners"], inplace=True)

#This should get rid of any duplicate entry
df.drop_duplicates(inplace=True)

# This should save any changes made before
df.to_csv("cleaned_steam.csv", index=False)

print("The bluetooth devi- I mean, the task has completed successfully!")