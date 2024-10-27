import cv2
import numpy as np
from config import CONFIG
import random

def apply_theme(image):
    theme = random.choice(CONFIG['themes'])  # Select a random theme
    
    if theme == 'vibrant':
        return cv2.convertScaleAbs(image, alpha=1.2, beta=10)
    elif theme == 'pastel':
        return cv2.addWeighted(image, 0.7, np.full_like(image, 255), 0.3, 0)
    elif theme == 'monochrome':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    elif theme == 'dark':
        return cv2.convertScaleAbs(image, alpha=0.8, beta=-50)
    else:
        return image