#helper class that processes the file
import numpy as np
from PIL import Image
import os
import time
#img = Image.open("C:\\mapper\\map1.jpg")
def processIMG(x, fileLocation, SeaLevelRise, interval):
    delta = abs(int(SeaLevelRise/interval))
    #hooray we get our maximum RGB value
    print("Processing Image....")
    #numpy array because python lists are slow
    pixels = np.array(x)
    #checking to see if the green channel is below the delta
    #who needs for loops when you can use vectorized operations
    below = pixels[:,:,0]<delta
    #setting that pixel to a bluish color
    pixels[below] = [0,41,58]
    #convert it backt to an image
    im2 = Image.fromarray(pixels.astype('uint8'))
    im2.show()
    #saving the image to directory
    timestr = time.strftime("%Y%m%d-%H%M%S")
    im2.save("Map" + timestr + ".jpg")
#testing with my dem of the United States processIMG(img, "", 1000,57.507) 