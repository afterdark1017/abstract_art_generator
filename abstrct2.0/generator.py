import cv2
import numpy as np
from art_types import *
from config import CONFIG
from themes import apply_theme

def generate_abstract_art():
    # Create a blank canvas
    canvas = np.zeros((CONFIG['image_height'], CONFIG['image_width'], 3), dtype=np.uint8)
    
    # Apply base color
    canvas[:] = CONFIG['base_color']
    
    # Apply random art types
    art_functions = [
        geometric_patterns.apply,
        layered_effects.apply,
        noise_patterns.apply,
        shapes.apply,
        symmetry_asymmetry.apply,
        algorithmic_art.apply,
        fractals.apply,
    ]
    
    np.random.shuffle(art_functions)
    num_layers = np.random.randint(CONFIG['min_layers'], CONFIG['max_layers'] + 1)
    
    for func in art_functions[:num_layers]:
        canvas = func(canvas)
    
    # Apply theme
    canvas = apply_theme(canvas)
    
    return canvas