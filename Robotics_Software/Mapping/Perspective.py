import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = mpimg.imread('example_grid1.jpg')
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

# Draw Source and destination points on images (in blue) before plotting
cv2.polylines(image, np.int32([source]), True, (0, 0, 255), 3)
cv2.polylines(warped, np.int32([destination]), True, (0, 0, 255), 3)
# Display the original image and binary
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(warped, cmap='gray')
ax2.set_title('Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()