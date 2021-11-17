import numpy as np
import os
from PIL import Image
from process import processIMG 
import time

try:
    max = int(input("Enter the maximum height: "))
except ValueError:
    print("Whoops that's not an int")
    max = int(input("Enter the maximum height: "))
try:
    min = int(input("Enter the minimum height (if it's below sea level it's negative): "))
except ValueError:
    print("Whoops that's not an int")
    min = int(input("Enter the minimum height (if it's below sea level it's negative): "))
difference = int(abs(max - min))
#blah blah how do I even do this
#split the difference into 256 separate parts
interval = difference/256
#needs to be a precise number
#how many meters/feet per pixel basically
#also can be shown as error
try:
    level = int(input("What height do you want the sea level to rise to?: "))
except ValueError:
    print("Whoops that's not an int")
    level = int(input("What height do you want the sea level to rise to?: "))
#get file from the user
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
print("OK file exists")
img = Image.open(user_input)
width, height = img.size
print("Your image is a",width,"x",height, img.format, " file")
start = time.time()
processIMG(img, user_input, level, interval)
end = time.time()
print("Processing is complete")
print("Here are some stats: ")
print("Processing took:", end-start, " seconds")
print("Error:±",interval, " ft")








    



