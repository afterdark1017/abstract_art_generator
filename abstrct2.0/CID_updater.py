import os
import json

# Path to the folder containing the metadata files
folder_path = r'C:\D\Desktop\abstrct2.0\abstract_art_output\metadata'

# The actual IPFS CID to replace the placeholder
ipfs_cid = 'QmRhFqCxbikWiVw6dVDzM88SaLmct97tKp2ZMqMvB19hdB'

print("Starting the update process...")

# Iterate over each file in the directory
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Open and read the file
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            # Check and replace the specific placeholder if present
            if 'QmbLxbiAJmtAfq3saetBxUF14AbTy4dz8zRg5UtUEdaUN7' in data['image']:
                data['image'] = data['image'].replace('QmbLxbiAJmtAfq3saetBxUF14AbTy4dz8zRg5UtUEdaUN7', ipfs_cid)
                # Write the updated data back to the file
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"File {index + 1} ({filename}) has been updated.")
            else:
                print(f"No placeholder 'your_actual_ipfs_cid_here' found in {filename}. No update needed.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {filename}.")
        except Exception as e:
            print(f"An error occurred with file {filename}: {e}")

print("Update process completed.")
