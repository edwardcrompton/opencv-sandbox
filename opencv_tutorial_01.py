# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("images/beech.jpeg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[300, 225]
print("R={}, G={}, B={}".format(R, G, B))

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 145, 150)
cv2.imwrite("images/edged-beech.jpeg", edged)

