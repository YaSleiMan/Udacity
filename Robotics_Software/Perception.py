# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Define the filename, read and plot the image
filename = 'sample.jpg'
#image_url = 'https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Rover+Example+Images/sample.jpg'
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()