print("Welcome to Mapper, a shittly written program to simulate changes of sea level")
print("I'm not sure how this even works but it works")
print("To run this program, you need a Digital Elevation Model (DEM)")
print("Please ensure that the provided dem is black and white (all values ranging from 0 - 255)")
print("If you don't have one why are you even running this program (Use arc gis to generate one)")
print("Please enter the MAX and MIN height values below")
MAXH = input("Maximum height: ")
MINH = input("Minimum height: ")
if not isinstance(int, MINH):
    print("Hello what are you doing? Enter it correctly")
    MAXH = input("Maximum height: ")
    MINH = input("Minimum height: ")



