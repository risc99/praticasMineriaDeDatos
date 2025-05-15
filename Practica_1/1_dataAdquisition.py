import kaggle
import os

# Ricardo Issac Sánchez Clark, Minería de datos 035
# I had to make a token, and put in in a .kaggle folder in my user folder

# A var with the name of the dataset in kaggle, the second var doesn't really do much, but whatevs
dataset_name = "nikdavis/steam-store-games"
file_name = "steam.csv"

# The commnad that downloads the dataset, don't know how insecure it is, probably a lot
os.system(f"kaggle datasets download -d {dataset_name} --force")

# Just a print, to be able to tell the end of the script in the terminal
print(f"Dataset {file_name} has been downloaded successfully!")
