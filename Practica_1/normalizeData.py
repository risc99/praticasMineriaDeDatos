import pandas as pd

# Ricardo Issac Sánchez Clark
# In the videos you explained that I needed to normilize the table for me to be able to analyze a few things, this is my attempt at it

df = pd.read_csv("cleaned_steam.csv")  # Adjust the path if needed

# The list of columns to normalize
multi_value_columns = ["developer", "publisher", "platforms", "categories", "genres", "steamspy_tags"]

# This should normalize each column, I think
for column in multi_value_columns:
    df[column] = df[column].str.split(";")
    df = df.explode(column)

df.to_csv("normalized_steam.csv", index=False)

print("The dataset has been normalized succesfully!")