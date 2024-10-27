import cv2
import numpy as np
from generator import generate_abstract_art
from config import CONFIG
import os
import json
from junk.metadata import generate_image_metadata  # Import the correct metadata generation function
from datetime import datetime  # Import datetime for timestamp

def create_output_folder():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Generate a timestamp
    folder_name = f"output_{timestamp}"  # Create folder name with timestamp
    output_folder = os.path.join(CONFIG['output_folder'], folder_name)
    
    if not os.path.exists(CONFIG['output_folder']):
        os.makedirs(CONFIG['output_folder'])
    
    os.makedirs(output_folder, exist_ok=True)
    return output_folder

def main():
    # Create output directories if they don't exist
    os.makedirs(CONFIG['image_folder'], exist_ok=True)
    os.makedirs(CONFIG['metadata_folder'], exist_ok=True)

    for i in range(CONFIG['num_images']):
        # Generate abstract art
        image = generate_abstract_art()
        
        # Save the image
        image_id = i + 1
        image_path = os.path.join(CONFIG['image_folder'], f"Fractal Flares {image_id}.png")
        cv2.imwrite(image_path, image)
        
        # Generate metadata and save it as a JSON file
        metadata = generate_image_metadata(image_id)  # Pass the image_id
        metadata_path = os.path.join(CONFIG['metadata_folder'], f"Fractal Flares {image_id}.json")
        with open(metadata_path, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
    
    print(f"Generated {CONFIG['num_images']} abstract art images in '{CONFIG['image_folder']}' and metadata in '{CONFIG['metadata_folder']}'")

if __name__ == "__main__":
    main()