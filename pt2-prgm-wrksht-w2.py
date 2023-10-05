# 

def speedCalculator():
    distance = int(input("Please enter the distance in metres as an integer: "))
    duration = int(input("Please enter the duration as minutes an integer: "))

    distanceKM = distance*1000
    durationHR = duration*60

    speed = distanceKM/durationHR
    print("Your speed is:",round(speed, 2),"km/h")
speedCalculator()

#

import math

def circumferenceOfCirlce():
    radius = float(input("Enter the radius of the circle"))
    circum = 2*math.pi*radius
    print("The circumference of the circle is:", round(circum, 2))
circumferenceOfCirlce()

# use of if and elif functions to provide the choice entering the radius or diameter

import math 

def circumferenceOfCirlce2():
    radius = str(input("Do you have a radius value? type ( y / n ) for your answer: "))
    radiusYes = ("y")
    radiusNo = ("n")
    if radius == radiusYes:
     radiusY = float(input("Please enter the radius value: "))
     circum2 = 2*math.pi*radiusY
     print("The circumference of the circle is:", round(circum2, 2))
    
    elif radius == radiusNo:
     diameter = float(input("Please enter the diameter value: "))
     radius2 = diameter/2
     circum2 = 2*math.pi*radius2
     print("The circumference of the circle is:", round(circum2, 2))
circumferenceOfCirlce2()

# 

def calcAreaOfCircle():
    radius = float(input("Enter the radius of the circle: "))
    areaofcircle = math.pi*(radius)**2
    print("The area of the rectangle is:", areaofcircle,)
calcAreaOfCircle()

#

def priceOfPizza():
    diameter = float(input("Enter the diameter of the pizza: "))
    priceOfPizza = diameter*0.35
    print("The price of the pizza is: £",priceOfPizza,)
priceOfPizza()    

#

def gradientSlopeCalc():
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))

    changeinx = x2-x1
    changeiny = y2-y1
    slope = changeiny/changeinx

    print("The gradient of the slope is:", slope)
gradientSlopeCalc()

# 

def distanceBetweenPoints():
    x1 = float(input("Please enter x1: "))
    y1 = float(input("Please enter y1: "))
    x2 = float(input("Please enter x2: "))
    y2 = float(input("Please enter y2: "))

    length = (x2-x1)**2
    height = (y2-y1)**2
    sqrtvalue = math.sqrt(length+height)
    distance = sqrtvalue

    print("The distance of the rectangle is:", round(distance, 2),"Metres")
distanceBetweenPoints()

#

def travelStatistics():
   averagespeed = float(input("Please enter the avergae speed in km/h: "))
   duration = float(input("Please enter the duration in hours: "))

   distancetravelled = averagespeed*duration
   fuelusage = distancetravelled*5
   print("Your distance travelled is:", round(distancetravelled, 2),"km", "and your fuel usage is", round(fuelusage, 2),"litres")
travelStatistics()

#

def sumOfSquares():
   n = int(input("Please enter the 'n' value: "))
   nlisted = 0
   for i in range(1):
      nlisted = 1**2 + 2**2 + n**2
      print("The total value is:", nlisted)
sumOfSquares()

# averageOfNumbers

num = int(input("How many numbers: "))
total_sum = 0
try:
    val = int(num)
    for n in range(val):
        numbers = float(input("enter a number: "))
        total_sum += numbers
    avg = total_sum/val

    print("average is: ", avg)
except ValueError:
    print("That is not a correct integer number, Try again")

# harder: function




  
