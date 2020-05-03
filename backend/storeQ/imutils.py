import numpy as np
import cv2

def resize(image, width=None, height=None):
    dim = None
    if width is None and height is None:
        return image
    if width is not None:
        # given width/(width of original image)
        aspectRatio = width / image.shape[1]
        dim = (width, int(image.shape[0]*aspectRatio))
    elif height is not None:
        # given height/(height of original image)
        aspectRatio = height / image.shape[0]
        dim = (int(image.shape[1]*aspectRatio), height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)