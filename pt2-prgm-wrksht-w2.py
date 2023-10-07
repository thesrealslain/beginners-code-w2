# first: basic function
# write a function named speedCalculator that asks the user for two integers: the distance travelled in km and the duration of the journey in hours
# speedCalculator should then output speed in kilometres per hour

def speedCalculator():
    distance = int(input("Please enter the distance in metres as an integer: "))
    duration = int(input("Please enter the duration as minutes an integer: "))

    distanceKM = distance*1000
    durationHR = duration*60

    speed = distanceKM/durationHR
    print("Your speed is:",round(speed, 2),"km/h")
speedCalculator()

# second: basic function
# write a function named circumferenceOfCircle that asks the user for the radius of a circle
# the function should then output (print) the circle’s circumference

import math

def circumferenceOfCirlce():
    radius = float(input("Enter the radius of the circle"))
    circum = 2*math.pi*radius
    print("The circumference of the circle is:", round(circum, 2))
circumferenceOfCirlce()

# the use of if and elif functions to provide the choice entering the radius or diameter

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

# third: basic function
# write a function named areaOfCircle that asks the user for the radius of a circle, it should then output the circle’s area

def calcAreaOfCircle():
    radius = float(input("Enter the radius of the circle: "))
    areaofcircle = math.pi*(radius)**2
    print("The area of the rectangle is:", areaofcircle,)
calcAreaOfCircle()

# fourth: basic function
# write a function named priceOfPizza that asks the user for the diameter of a pizza (in cm) your function should then output the cost of the pizza (based on its area) in pounds
# assume that the cost of the ingredients is 3.5 pence per square cm


def priceOfPizza():
    diameter = float(input("Enter the diameter of the pizza: "))
    priceOfPizza = diameter*0.35
    print("The price of the pizza is: £",priceOfPizza,)
priceOfPizza()    

# fifth: basic function
# write a function named slopeOfLine that first asks the user for four values x1, y1, x2 and y2 that represent two points in two-dimensional space
# (i.e. points with coordinates (x1, y1) and (x2, y2)), the function should then output the slope of the line that connects them

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

# sixth: basic function
# write a function named distanceBetweenPoints that asks the user for four values x1, y1, x2 and y2 that represent two points in two-dimensional space,
# and then outputs the distance between them

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

# seventh: basic function
# write a function named travelStatistics which asks the user to input the average speed (in km/hour) and duration (in hours) of a car journey
# the function should then output the overall distance travelled (in km), and the amount of fuel used (in litres) assuming a fuel efficiency of 5 km/litre

def travelStatistics():
   averagespeed = float(input("Please enter the avergae speed in km/h: "))
   duration = float(input("Please enter the duration in hours: "))

   distancetravelled = averagespeed*duration
   fuelusage = distancetravelled*5
   print("Your distance travelled is:", round(distancetravelled, 2),"km", "and your fuel usage is", round(fuelusage, 2),"litres")
travelStatistics()

# eighth: basic function
# write a function named sumOfSquares that uses a loop to output the sum 1**2 + 2**2 + … + n**2 where n is an integer provided by the user,
# for example, if the user enters 3, the function should output 14 (1**2 + 2**2 + 3**2)

def sumOfSquares():
   n = int(input("Please enter the 'n' value: "))
   nlisted = 0
   for i in range(1):
      nlisted = 1**2 + 2**2 + n**2
      print("The total value is:", nlisted)
sumOfSquares()

# ninth: basic function
# write a function averageOfNumbers which outputs the average of a series of numbers entered by the user,
# the function should first ask the user how many numbers there are to be inputted

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

# tenth: harder function
# write a function named fibonacci which asks the user for a number n, use a loop to calculate and output the nth value in the Fibonacci sequence,
# hint: once again, you don’t need to use lists or if statements

list = []

n = int(input("Enter the length of your fibonacci sequence: "))

n1 = 0
n2 = 1
count = 2

if n < 0:
    print("Please only enter positive numbers!")
elif n == 1:
    print(n1)
else:
    print(n1, end=" ")
    print(n2, end=" ")
    while count<n:
        n3 = n1+n2
        print(n3, end=" ")
        count+=1
        n1=n2
        n2=n3


# eleventh: harder function
# write a function selectCoins that asks the user an amount of money in pence, it should output the number of coins of each denomination (£2 to 1p) that should be used to make up that amount,
# for example, if the input is 292 pence, then the function should report the following: 1 × £2, 0 × £1, 1 × 50p, 2 × 20p, 0 × 10p, 0 × 5p, 1 × 2p, 0 × 1p,
# hint: use integer division and the remainder (modulo), if you know lists in python, write another version of this function, selectCoins2, that uses lists 

def selectCoins():
    coins = int(input("Please enter your amount in pennies: "))
    
    coins2Pnds = coins//200
    coinsLeft = coins%200
    
    coins1Pnds = coinsLeft//100
    coinsLeft = coinsLeft%100

    coins50p = coinsLeft//50
    coinsLeft = coinsLeft%50
    
    coins20p = coinsLeft//20
    coinsLeft = coinsLeft%20

    coins10p = coinsLeft//10
    coinsLeft = coinsLeft%10

    coins5p = coinsLeft//5
    coinsLeft = coinsLeft%5

    coins2p = coinsLeft//2
    coinsLeft = coinsLeft%2

    coins1p = coinsLeft//1
    coinsLeft = coinsLeft%1

    if(coins == 0):
        print("N0 change")
    
    if(coins2Pnds == 1):
        print(coins2Pnds,"x £2")
    elif(coins2Pnds>0):
        print(coins2Pnds,"x £2s")

    
    if(coins1Pnds == 1):
        print(coins1Pnds,"x £1")
    elif(coins1Pnds>0):
        print(coins1Pnds,"x £1s")


    if(coins50p == 1):
        print(coins50p,"x 50p")
    elif(coins50p>0):
        print(coins50p,"x 50ps")


    if(coins20p == 1):
        print(coins20p,"x 20p")
    elif(coins20p>0):
        print(coins20p,"x 20ps")

    
    if(coins10p == 1):
        print(coins10p,"x 10p")
    elif(coins10p>0):
        print(coins10p,"x 10ps")

    
    if(coins5p == 1):
        print(coins5p,"x 5p")
    elif(coins5p>0):
        print(coins5p,"x 5ps")

    
    if(coins2p == 1):
        print(coins2p,"x 2p")
    elif(coins2p>0):
        print(coins2p,"x 2ps")

    
    if(coins1p == 1):
        print(coins1p,"x 1p")
    elif(coins1p>0):
        print(coins1p,"x 1ps")
selectCoins()


  
