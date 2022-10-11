import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = mpimg.imread('example_grid1.jpg')
plt.imshow(image)
plt.show()
# point coordinates: [14.7278,139.985] / [119.301,95.7843] / [200.157,95.7843] / [302.574,139.446]

def perspect_transform(img, src, dst):
    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped

# Define source and destination points
source = np.float32([[14.7278,139.985],[119.301,95.7843],[200.157,95.7843],[302.574,139.446]])
destination = np.float32([[145,155], [145,145], [155,145], [155,155]])

warped = perspect_transform(image, source, destination)
plt.imshow(warped)
plt.show()
