
import numpy as np
from scipy import signal
from PIL import Image


def load_image_path(path):
    return np.asarray(Image.open(path))/255.0

def save(path, img):
    tmp = np.asarray(img*255.0, dtype=np.uint8)
    Image.fromarray(tmp).save(path)

def remove_noise_image(inp):
    # estimate 'background' color by a median filter
    bg = signal.medfilt2d(inp,11)
    save('images/background_estimation.jpeg', bg)

    # compute 'foreground' mask as anything that is significantly darker than
    # the background
    mask = inp < bg - 0.1
    save('images/foreground_mask.jpeg', mask)

    # return the input value for all pixels in the mask or pure white otherwise
    return np.where(mask, inp, 1.0)

#load the file
image = Image.open('1.jpeg')

#convert image to grayscale
image = image.convert('L')

#resize the image
new_image = image.resize((832, 536))  

#now carry out the operations on modified image
new_image.save('images/modified_image.jpeg')
inp_destination = 'images/modified_image.jpeg'
out_destination = 'images/output_image.jpeg'

input = load_image_path(inp_destination)
output = remove_noise_image(input)

save(out_destination, output)
