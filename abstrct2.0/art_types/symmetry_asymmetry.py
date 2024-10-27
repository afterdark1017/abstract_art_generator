import cv2
import numpy as np

def apply(image):
    choice = np.random.choice(['vertical', 'horizontal', 'both'])
    
    if choice == 'vertical':
        left = image[:, :image.shape[1]//2]
        right = cv2.flip(left, 1)
        image = np.hstack((left, right))
    elif choice == 'horizontal':
        top = image[:image.shape[0]//2, :]
        bottom = cv2.flip(top, 0)
        image = np.vstack((top, bottom))
    else:  # both
        quarter = image[:image.shape[0]//2, :image.shape[1]//2]
        right = cv2.flip(quarter, 1)
        top = np.hstack((quarter, right))
        bottom = cv2.flip(top, 0)
        image = np.vstack((top, bottom))
    
    return image