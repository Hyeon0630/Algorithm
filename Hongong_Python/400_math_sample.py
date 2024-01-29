import math

class Circle():
    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 2*math.pi*self.r
    
    def area(self):
        return self.r*self.r*math.pi
    
circle = Circle(10)
print("원의 둘레:", circle.circumference())
print("원의 넓이:", circle.area())