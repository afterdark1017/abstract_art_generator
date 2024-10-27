import os

# Path to the directory containing the images
directory = 'abstract_art_output/images/'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.startswith("Fractal Flares "):  # Check if the filename starts with the prefix
        new_name = filename.replace("Fractal Flares ", "")  # Create the new name
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))  # Rename the file

