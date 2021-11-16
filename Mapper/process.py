#helper class that processes the file
import numpy as np
from PIL import Image

def processIMG(Image, fileLocation, SeaLevelRise, interval):
    delta = abs(int(interval * SeaLevelRise))
    Image.show()
    #hooray we get our maximum RGB value
    print("Processing Image....")
    #numpy array because python lists are slow
    pixels = np.array(Image)
    red, green, blue= pixels.T 
    lowAreas = (red<delta) &(blue<delta) &(red<delta)
    pixels[..., :-1][lowAreas.T] = (255, 0, 0)
    im2 = Image.fromarray(pixels)
    im2.show()