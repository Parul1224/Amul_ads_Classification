import cv2
import numpy as np
import Image

#inpuut the image
imageFileName = raw_input("enter the image name with absolute path ")

image1 = Image.open(imageFileName)
#img=cv2.imread(imageFileName)

#transform into numpy array so as to processed by the cv2 functions
img = np.asarray(image1)

#change the colour-space
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#apply canny edge detection
edges = cv2.Canny(gray,50,150,apertureSize = 3)

#specify the constraints
minLineLength = 400
maxLineGap = 15

#remove the borders from image
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)

#display the image
cv2.imshow('GRIDS_REMOVED', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/removed_grids.jpeg', img)
    cv2.destroyAllWindows()
