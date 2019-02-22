# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("images/beech.jpeg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

