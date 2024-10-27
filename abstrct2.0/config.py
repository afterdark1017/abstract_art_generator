import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    'num_images': 10000,
    'image_width': 512,
    'image_height': 512,
    'base_color': (255, 255, 255),  # White
    'min_layers': 3,
    'max_layers': 7,
    'color_palette': [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
    ],
    'themes': ['vibrant', 'pastel', 'monochrome', 'dark'],  # List of available themes
    'output_folder': os.path.join(PROJECT_ROOT, 'abstract_art_output'),
    'image_folder': os.path.join(PROJECT_ROOT, 'abstract_art_output', 'images'),
    'metadata_folder': os.path.join(PROJECT_ROOT, 'abstract_art_output', 'metadata')
}