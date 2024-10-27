import cv2
import numpy as np
from numba import jit
from config import CONFIG

@jit(nopython=True)
def mandelbrot(h, w, max_iter, x_min, x_max, y_min, y_max):
    y = np.linspace(y_min, y_max, h)
    x = np.linspace(x_min, x_max, w)
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]
    z = np.zeros_like(c)
    divtime = np.zeros((h, w), dtype=np.int32)

    for i in range(max_iter):
        z = z**2 + c
        diverge = np.abs(z) > 2
        for row in range(h):
            for col in range(w):
                if diverge[row, col] and divtime[row, col] == 0:
                    divtime[row, col] = i
                if diverge[row, col]:
                    z[row, col] = 2 + 0j

    return divtime

@jit(nopython=True)
def julia(h, w, max_iter, c, x_min, x_max, y_min, y_max):
    y = np.linspace(y_min, y_max, h)
    x = np.linspace(x_min, x_max, w)
    z = x[:, np.newaxis] + 1j * y[np.newaxis, :]
    divtime = np.zeros((h, w), dtype=np.int32)

    for i in range(max_iter):
        z = z**2 + c
        diverge = np.abs(z) > 2
        for row in range(h):
            for col in range(w):
                if diverge[row, col] and divtime[row, col] == 0:
                    divtime[row, col] = i
                if diverge[row, col]:
                    z[row, col] = 2 + 0j

    return divtime

@jit(nopython=True)
def apply_color_gradient(fractal, max_iter):
    normalized = fractal / max_iter
    colored = np.zeros((fractal.shape[0], fractal.shape[1], 3), dtype=np.uint8)

    colored[:, :, 0] = np.sin(normalized * np.pi) * 255
    colored[:, :, 1] = np.sin(normalized * np.pi * 2) * 255
    colored[:, :, 2] = np.sin(normalized * np.pi * 4) * 255

    return colored

def apply(image):
    h, w = image.shape[:2]
    max_iter = 1000

    fractal_type = np.random.choice(['mandelbrot', 'julia'])

    if fractal_type == 'mandelbrot':
        x_min, x_max = np.random.uniform(-2, 0), np.random.uniform(0, 1)
        y_min, y_max = np.random.uniform(-1.5, 0), np.random.uniform(0, 1.5)
        fractal = mandelbrot(h, w, max_iter, x_min, x_max, y_min, y_max)
    else:  # julia
        c = complex(np.random.uniform(-1, 1), np.random.uniform(-1, 1))
        x_min, x_max = np.random.uniform(-2, 0), np.random.uniform(0, 2)
        y_min, y_max = np.random.uniform(-1.5, 0), np.random.uniform(0, 1.5)
        fractal = julia(h, w, max_iter, c, x_min, x_max, y_min, y_max)

    fractal_color = apply_color_gradient(fractal, max_iter)

    # Apply a zoom effect
    zoom_center = (np.random.randint(w), np.random.randint(h))
    zoom_scale = np.random.uniform(1.5, 3)
    M = cv2.getRotationMatrix2D(zoom_center, 0, zoom_scale)
    fractal_color = cv2.warpAffine(fractal_color, M, (w, h))

    # Add some post-processing effects
    fractal_color = cv2.GaussianBlur(fractal_color, (5, 5), 0)
    fractal_color = cv2.addWeighted(fractal_color, 1.2, fractal_color, 0, 10)

    return cv2.addWeighted(image, 0.3, fractal_color, 0.7, 0)