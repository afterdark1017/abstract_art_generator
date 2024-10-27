import cv2
import numpy as np
from config import CONFIG

def apply(image):
    shape = np.random.choice(['circle', 'rectangle', 'triangle'])
    color = tuple(map(int, CONFIG['color_palette'][np.random.randint(len(CONFIG['color_palette']))]))
    
    if shape == 'circle':
        center = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
        radius = np.random.randint(50, 200)
        cv2.circle(image, center, radius, color, -1)
    elif shape == 'rectangle':
        pt1 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
        pt2 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
        cv2.rectangle(image, pt1, pt2, color, -1)
    else:  # triangle
        pts = np.array([
            [np.random.randint(image.shape[1]), np.random.randint(image.shape[0])],
            [np.random.randint(image.shape[1]), np.random.randint(image.shape[0])],
            [np.random.randint(image.shape[1]), np.random.randint(image.shape[0])]
        ], np.int32)
        cv2.fillPoly(image, [pts], color)
    
    return image