import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from Function_Dump import color_thresh
from Function_Dump import perspect_transform

# Read in the same sample image as before
image = mpimg.imread('sample.jpg')
source = np.float32([[14.7278,139.985],[119.301,95.7843],[200.157,95.7843],[302.574,139.446]])
destination = np.float32([[155,160], [155,150], [165,150], [165,160]])

# Assume you have already defined perspect_transform() and color_thresh()
warped = perspect_transform(image, source, destination)
colorsel = color_thresh(warped, rgb_thresh=(160, 160, 160))

# Plot the result
plt.imshow(colorsel, cmap='gray')
plt.show()

ypos, xpos = colorsel.nonzero()
plt.plot(xpos, ypos, '.')
plt.xlim(0, 320)
plt.ylim(0, 160)
plt.show()

def rover_coords(binary_img):
    # Extract xpos and ypos pixel positions from binary_img and
    # Convert xpos and ypos to rover-centric coordinates
    ypos, xpos = binary_img.nonzero()
    x_pixel = np.zeros(len(xpos),dtype=int)
    y_pixel = np.zeros(len(ypos),dtype=int)
    for i in range(len(xpos)):
        x_pixel[i] = xpos[i]-160
    for i in range(len(ypos)):
        y_pixel[i] = 160-ypos[i]
    #x_pixel = -(ypos - binary_img.shape[0]).astype(np.float)
    #y_pixel = -(xpos - binary_img.shape[1] / 2).astype(np.float)
    return x_pixel, y_pixel

ypos, xpos = rover_coords(colorsel)
plt.plot(xpos, ypos, '.')
plt.xlim(0, 160)
plt.ylim(-160, 160)
plt.show()