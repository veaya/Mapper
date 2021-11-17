# Mapper

A simple python program to simulate a rising sea level on multiple different DEMS (Digital Elevation Model)

## Requirements

You need Pillow and NumPy
```bash
pip install PIL
```
```bash
pip install numpy
```
## Usage
You need a greyscale linearly scaled DEM preferable in JPG or similar formats  

(Black (255,255,255) is lowest, White (0,0,0)  is highest)

PLEASE PLEASE PLEASE if you're using a mask make sure it maxes out the red value or it may get overwritten

Copy included python files anywhere onto your disk and run 'main' in a console environment

## Contributing
I'm new to Github so I dont know how contributing works, but send me a message if you want to!

## Parameters
MinHeight = lowest elevation present on DEM  
MaxHeight = highest elevation available on DEM  
SeaLevelRise = the height you want the sea level to rise to  
FilePath = Where you want to read the image from and save the image to
## Examples
Before processing:![image](https://user-images.githubusercontent.com/91225760/142093365-ddf3829f-fe20-4fb1-a7d3-cbd0ac596a2b.png)
After processing with 1500 foot sea rise: ![image](https://user-images.githubusercontent.com/91225760/142093572-aaa0b160-6c71-411f-bdd8-7c3fa5f89ff4.png)
Sample input:![image](https://user-images.githubusercontent.com/91225760/142093720-68d29716-2729-47d1-a9b0-69f422cd863b.png)





