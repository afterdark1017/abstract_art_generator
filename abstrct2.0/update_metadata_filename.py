import os

# Directory containing the JSON files
directory = r'C:\D\Desktop\abstrct2.0\abstract_art_output\metadata'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.startswith("Fractal Flares ") and filename.endswith(".json"):
        # Construct the old file path
        old_file = os.path.join(directory, filename)
        
        # Remove the prefix and construct the new file path
        new_filename = filename.replace("Fractal Flares ", "")
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed "{old_file}" to "{new_file}"')

