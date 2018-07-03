

from pytesseract import image_to_string
from PIL import Image
imageFileName = raw_input("enter the image name with absolute path ")
im = Image.open(imageFileName)
print(image_to_string(im))  



