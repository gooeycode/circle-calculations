from circleclass import Circle
import time

#declerations
circleOne = Circle()
circleTwo = Circle()
REPROMPT = "enter radius higher than 0."
ZERO = 0

#detailLoop
print("input radius")
radiusInput = input()

while (int(radiusInput) <= ZERO):
    print(REPROMPT)
    radiusInput = input()

circleOne.setRadius(int(radiusInput))
circleOne.calculateArea(int(radiusInput))
circleOne.calculateDiameter(int(radiusInput))
time.sleep(2)
print( "Radius entered is:", circleOne.getRadius() )
time.sleep(2)
print( "Area is:", circleOne.getArea())
time.sleep(2)
print( "Diameter is:", circleOne.getDiameter())

print("")

time.sleep(2)

print ("Circle 2 will be using the constructor radius.")
circleTwo.calculateArea(circleTwo.getRadius())
circleTwo.calculateDiameter(circleTwo.getRadius())
time.sleep(2)
print("Constructor radius is: ", circleTwo.getRadius() )
time.sleep(2)
print("Area is:", circleTwo.getArea())
time.sleep(2)
print("Diameter is:", circleTwo.getDiameter())

time.sleep(2)

print ("Thank you for using this program, goodbye")

time.sleep(2)