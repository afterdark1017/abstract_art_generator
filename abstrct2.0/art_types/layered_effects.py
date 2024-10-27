import cv2
import numpy as np
from config import CONFIG

def apply(image):
    overlay = np.zeros_like(image)
    color = tuple(map(int, CONFIG['color_palette'][np.random.randint(len(CONFIG['color_palette']))]))
    cv2.rectangle(overlay, (0, 0), (image.shape[1], image.shape[0]), color, -1)
    
    alpha = np.random.uniform(0.2, 0.5)
    return cv2.addWeighted(image, 1, overlay, alpha, 0)