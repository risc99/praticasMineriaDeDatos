import zipfile

# Ricardo Issac Sánchez Clark, Minería de datos 035
# I could have extracted it manually, but I didn't know if it was part of the assingment

# A var for the name of the zip
zip_file = "steam-store-games.zip"

# This should extract the zip in a folder called steam_dataset
with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall("steam_dataset")

# Again, just printing to find the end of the script in the terminal
print("Dataset extracted successfully!")