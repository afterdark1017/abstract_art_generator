import cv2
import numpy as np
from config import CONFIG

def apply(image):
    num_shapes = np.random.randint(5, 20)
    for _ in range(num_shapes):
        shape_type = np.random.choice(['circle', 'rectangle', 'line'])
        color = tuple(map(int, CONFIG['color_palette'][np.random.randint(len(CONFIG['color_palette']))]))
        
        if shape_type == 'circle':
            center = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
            radius = np.random.randint(10, 50)
            cv2.circle(image, center, radius, color, 2)
        elif shape_type == 'rectangle':
            pt1 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
            pt2 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
            cv2.rectangle(image, pt1, pt2, color, 2)
        else:  # line
            pt1 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
            pt2 = (np.random.randint(image.shape[1]), np.random.randint(image.shape[0]))
            cv2.line(image, pt1, pt2, color, 2)
    
    return image