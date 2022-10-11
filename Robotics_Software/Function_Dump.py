import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import numpy as np

def color_thresh(img, rgb_thresh=(0, 0, 0)):
    binary_image = np.zeros(img.shape[0:2])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if(img[i,j,k]>rgb_thresh[k]):
                    binary_image[i,j]=1
    return binary_image

def perspect_transform(img, src, dst):
    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped