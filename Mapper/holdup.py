
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


    



