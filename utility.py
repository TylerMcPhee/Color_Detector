import numpy as np
import cv2

def get_HSV_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerlim = hsvC[0][0][0] - 10, 100, 100
    upperlim = hsvC[0][0][0] + 10, 255, 255

    lowerlim = np.array(lowerlim, dtype = np.uint8)
    upperlim = np.array(upperlim, dtype = np.uint8)

    return lowerlim, upperlim
   

# def in_range_HSV(src, lower, upper):
#     # Initialize mask with zeros (black)
#     mask = np.zeros(src.shape[:2], dtype=np.uint8)
    
#     # Check if each pixel's channels are within bounds
#     for i in range(src.shape[0]):      # Rows (height)
#         for j in range(src.shape[1]):  # Columns (width)
#             pixel = src[i, j]
#             in_range = True
#             for k in range(src.shape[2]):  # Channels (e.g., H,S,V)
#                 if not (lower[k] <= pixel[k] <= upper[k]):
#                     in_range = False
#                     break
#             if in_range:
#                 mask[i, j] = 255  # White pixel
#     return mask




# def get_RGB_limits(color, tolerance=100):
    
#     color = np.array(color, dtype=np.uint8)
#     lower = np.array([max(0, c - tolerance) for c in color], dtype=np.uint8)
#     upper = np.array([min(255, c + tolerance) for c in color], dtype=np.uint8)
#     return lower, upper

# def in_range_rgb(image, lower, upper):
#     return cv2.inRange(image, lower, upper)