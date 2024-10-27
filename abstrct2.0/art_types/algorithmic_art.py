import cv2
import numpy as np

def apply(image):
    rows, cols = image.shape[:2]
    
    # Create a grid of x and y coordinates
    x = np.linspace(0, 1, cols)
    y = np.linspace(0, 1, rows)
    xv, yv = np.meshgrid(x, y)
    
    # Apply a mathematical function to create a pattern
    z = np.sin(10 * xv) * np.cos(10 * yv)
    
    # Normalize the result to 0-255 range
    z = ((z - z.min()) / (z.max() - z.min()) * 255).astype(np.uint8)
    
    # Apply the pattern to the image
    pattern = cv2.merge([z, z, z])
    return cv2.addWeighted(image, 0.7, pattern, 0.3, 0)