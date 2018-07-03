import cv2
import numpy as np
import pytesseract
from PIL import Image
import subprocess

# Path of working folder on Disk
src_path = '2.jpeg'

#def get_string(img_path):
    

image=cv2.imread('2.jpeg')
    # Convert to gray
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
cv2.imwrite('sr_path' + "removed_noise.jpg", img)

    #  Apply threshold to get image with only black and white
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

   
    # Recognize text with tesseract for python
im = Image.open(src_path)
im.show()
print pytesseract.image_to_string(im)

