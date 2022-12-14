# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Define the filename, read and plot the image
filename = 'sample.jpg'
#image_url = 'https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Rover+Example+Images/sample.jpg'
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()

############

print(image.dtype, image.shape, np.min(image), np.max(image))
# uint8 (160, 320, 3) 0 255

# Note: we use the np.copy() function rather than just saying red_channel = image
# because in Python, such a statement would set those two arrays equal to each other
# forever, meaning any changes made to one would also be made to the other!
red_channel = np.copy(image)
# Note: here instead of extracting individual channels from the image
# I'll keep all 3 color channels in each case but set the ones I'm not interested
# in to zero.
red_channel[:,:,[1, 2]] = 0 # Zero out the green and blue channels
green_channel = np.copy(image)
green_channel[:,:,[0, 2]] = 0 # Zero out the red and blue channels
blue_channel = np.copy(image)
blue_channel[:,:,[0, 1]] = 0 # Zero out the red and green channels
fig = plt.figure(figsize=(12,3)) # Create a figure for plotting
plt.subplot(131) # Initialize subplot number 1 in a figure that is 3 columns 1 row
plt.imshow(red_channel) # Plot the red channel
plt.subplot(132) # Initialize subplot number 2 in a figure that is 3 columns 1 row
plt.imshow(green_channel)  # Plot the green channel
plt.subplot(133) # Initialize subplot number 3 in a figure that is 3 columns 1 row
plt.imshow(blue_channel)  # Plot the blue channel
plt.show()

##########

# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    binary_image = np.zeros(img.shape[0:2])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if(img[i,j,k]>rgb_thresh[k]):
                    binary_image[i,j]=1
    return binary_image

binary_image = color_thresh(image,[160,160,160])
plt.imshow(binary_image)
plt.show()
