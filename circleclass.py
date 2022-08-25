#circle class, fields, attributes and methods

from multiprocessing.heap import Arena

class Circle:

#setter methods
    def __init__(self):
        self.radius = 1
    
    def setRadius(self, radius):
        print ("setter method for radius called")
        if (radius <= 0):
            raise ValueError("radius needs to be more than 0")
            print("enter radius")
        else:
            self.radius = radius
            print ("Radius has been set to:", self.radius)
        return self.radius

#calculate methods

    def calculateDiameter(self, radius):
        two = 2
        diameter = radius * two
        self.diameter = diameter
        return self.diameter
    
    def calculateArea(self, radius):
        pi = 3.14
        area = (radius * radius) * pi
        self.area = area
        return self.area
    
#get methods
    def getRadius(self):
        return self.radius
    
    def getArea(self):
        return self.area
    
    def getDiameter(self):
        return self.diameter

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

circleTwo.calculateArea(int(radiusInput))
circleTwo.calculateDiameter(int(radiusInput))
print("Radius entered is: ", circleTwo.getRadius() )
print("Area is:", circleTwo.getArea())
print("Diameter is:", circleTwo.getDiameter())
74