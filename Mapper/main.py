#main class
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

#Finding the height that a single color increment is worth
difference = int(abs(max - min))
interval = difference/256

try:
    level = int(input("What height do you want the sea level to rise to?: "))
except ValueError:
    print("Whoops that's not an int")
    level = int(input("What height do you want the sea level to rise to?: "))

#getting file from the user
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
print("OK file exists")
img = Image.open(user_input)

#printing file details
width, height = img.size
print("Your image is a",width,"x",height, img.format, " file")

#time it because why not
start = time.time()
processIMG(img, user_input, level, interval)
end = time.time()

#printing a bunch of random stuff
print("Processing is complete")
print("Here are some stats: ")
print("Processing took:", end-start, " seconds")
print("Error: ±",interval, " ft")








    



