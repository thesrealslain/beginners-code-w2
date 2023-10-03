import math

# first function
# this function calculates the square root of a non-negative number from inputted values from a user 

def squareRootCalculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers")
    else:
        sqrtValue = math.sqrt(num)
        print("Square root:", round(sqrtValue,2))
squareRootCalculator()

# second function
# this function calculates the sine and cosine values of an angle from inputted values from a user

def sineAndCosine():
    angle = float(input("Enter an angle in degrees: "))
    angleInRadians = math.radians(angle)
    sineValue = math.sin(angleInRadians)
    cosineValue = math.cos(angleInRadians)
    print("sine of the angle:", round(sineValue, 2))
    print("Cosine of the angle", round(cosineValue, 2))
sineAndCosine()

# third function 
# this function calculates the area of a rectangle using inputted values from a user

def calcArea():
    lengthVal = float(input("Enter the length of the rectangle (metres): "))
    heightVal = float(input("Enter the height of the rectangle (metres): "))
    areaofrec = heightVal*lengthVal
    print("The area of the rectangle is:", areaofrec,"M*2")
calcArea()

# fourth function
# this function calculates the area a rectangle from top left point and bottom right point,
# from values inputted from a user 

def areaofrec2():
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))

    length = x2-x1
    height = y2-y1
    area = length*height

    print("The area of the rectangle is:", area, "M*2")
areaofrec2()

# fifth function 
# this function calculates the distance between two points from values inputted from a user

import math

def areaofrec3():
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))

    length = (x2-x1)**2
    height = (y2-y1)**2
    sqrtvalue = math.sqrt(length+height)
    distance = sqrtvalue

    print("The distance of the rectangle is:", round(distance, 2),"Metres")
areaofrec3()

