import math

class Circle():
    def __init__(self, r):
        if r <= 0:
            raise TypeError("길이는 양의 숫자")
        else:
            self.__r = r

    def circumference(self):
        return 2*math.pi*self.__r
    
    def area(self):
        return self.__r*self.__r*math.pi
    
    @property
    def r(self):
        return self.__r
    
    @r.setter
    def r(self, r):
        if r <= 0:
            raise TypeError("길이는 양의 숫자")
        else:
            self.__r = r
    
circle = Circle(10)
print("원래 원의 반지름:", circle.r)
circle.r = 2
print("변경된 원의 반지름:", circle.r)