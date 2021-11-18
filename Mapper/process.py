#helper class that processes the file
import numpy as np
from PIL import Image
import os
import time

def processIMG(x, fileLocation, SeaLevelRise, interval):
    #hooray we get our maximum RGB value
    delta = abs(int(SeaLevelRise/interval))
    print("Processing Image....")
    
    #numpy array because they're fast
    #also they're vectorized AKA no loops
    pixels = np.array(x)
   
    #check to see if all the pixels' red channels are below the delta (0-256)
    below = pixels[:,:,0] < delta
    
    #setting all those pixels to a bluish color
    pixels[below] = [0,41,58]
    
    #convert it back to an image
    im2 = Image.fromarray(pixels.astype('uint8'))
    
    #show it cause why not
    im2.show()
    
    #saving the image back to the directory
    timestr = time.strftime("%Y%m%d-%H%M%S")
    im2.save("Map" + timestr + ".jpg")
