import numpy as np
import os
from PIL import Image
from process import what 
#if we try to open a big file we can shut pillow up
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)

try:
    max = int(input("Enter the maximum height: "))
except ValueError:
    print("Whoops that's not an int")
    max = int(input("Enter the maximum height: "))
try:
    min = int(input("Enter the minimum height: "))
except ValueError:
    print("Whoops that's not an int")
    min = int(input("Enter the minimum height: "))
difference = int(abs(max - min))
#blah blah how do I even do this
#split the difference into 256 separate parts
interval = int(difference/256)
#you can already tell that this is being created without accuracy in mind
#simply due to the limitations of rgb
try:
    level = int(input("What height do you want the sea level to rise to?: "))
except ValueError:
    print("Whoops that's not an int")
    level = int(input("What height do you want the sea level to rise to?: "))
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("OK file exists")
img = Image.open(user_input)

print(img.format)

what(user_input, level, interval)
#stuff you do with the file goes here
f.close()






    



