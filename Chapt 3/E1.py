width = float(input("Please enter width: "))
length = float(input("Please enter length: "))
area = round(width*length,2)

if width == length:
    print("This is a square of area", area)
else:
    print("This is a rectangle of area", area)