import math

class Circle():
    def __init__(self, r):
        self.__r = r

    def circumference(self):
        return 2*math.pi*self.__r
    
    def area(self):
        return self.__r*self.__r*math.pi
    
circle = Circle(10)
print("원의 둘레:", circle.circumference())
print("원의 넓이:", circle.area())

print()
print("# __r에 접근합니다.")
print(circle.__r)