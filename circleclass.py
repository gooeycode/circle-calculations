#circle class, fields, attributes and methods

from multiprocessing.heap import Arena

class Circle:

#setter methods
    def __init__(self):
        self.radius = 1
    
    def setRadius(self, radius):
        if (radius <= 0):
            raise ValueError("radius needs to be more than 0")
            print("enter radius")
        else:
            self.radius = radius
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