import circleclass

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
print( "Radius entered is: ", circleOne.getRadius() )
print( "Area is:", circleOne.getArea())
print( "Diameter is:", circleOne.getDiameter())

circleTwo.setRadius()
circleTwo.calculateArea(int(radiusInput))
circleTwo.calculateDiameter(int(radiusInput))
print("Radius entered is: ", circleTwo.getRadius() )
print("Area is:", circleTwo.getArea())
print("Diameter is:", circleTwo.getDiameter())
