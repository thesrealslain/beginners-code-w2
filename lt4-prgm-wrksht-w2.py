import math

# this function is to calculate the square root of a non-negative number

def squareRootCalculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers")
    else:
        sqrtValue = math.sqrt(num)
        print("Square root:", round(sqrtValue,2))
squareRootCalculator()

# this function is to calculate the sine and cosine values of an angle

def sineAndCosine():
    angle = float(input("Enter an angle in degrees: "))
    angleInRadians = math.radians(angle)
    sineValue = math.sin(angleInRadians)
    cosineValue = math.cos(angleInRadians)
    print("sine of the angle:", round(sineValue, 2))
    print("Cosine of the angle", round(cosineValue, 2))
sineAndCosine()


