import cv2
import numpy as np

def apply(image):
    noise = np.random.normal(0, 50, image.shape).astype(np.uint8)
    return cv2.add(image, noise)