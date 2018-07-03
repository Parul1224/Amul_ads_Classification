
#-*- coding: utf-8 -*-
import cv2
import numpy as np
import Image
import os

imageFileName = raw_input("enter the image name with absolute path ")

image1 = Image.open(imageFileName);

image = np.asarray(image1)

#load an image from using this command
#image = cv2.imread(image1)

#Changing the color-space to simplify the operation (here changing to scale->GRAY)
modified = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Specify the structural element as per the requirement for carrying out the morphological opeartions,here we have chose Ellipse
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

#Carry out the erosion operation for removing noise
erosion = cv2.erode(modified,kernel,iterations = 1)


#Carry out the dilation operation for removing noise
dilation = cv2.dilate(modified,kernel,iterations = 1)


#Difference between the dilation and erosion of image
grad = cv2.morphologyEx(modified, cv2.MORPH_GRADIENT, kernel)


#Assigning the best threshold to the graysacle image (Otsus Binarization or Binary ,whichever suits best)
_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


#Now choosing the structuring element as Rectangle
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))


#Now again calculating the difference between the  erosion and deletion
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

#Finding contours
img, contours, _= cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#Array depending upon the shape filled with zeroes (used later)
mask = np.zeros(bw.shape, dtype=np.uint8)


#Drawing rectangles around the texts and modifying the graysacle image "modified"
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

    if r > 0.45 and w > 8 and h > 8:
        cv2.rectangle(image, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)


#Displaying the image with bounding box around the texts
cv2.imshow('rects', image)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/detected_text.jpg', image)
    cv2.destroyAllWindows()
