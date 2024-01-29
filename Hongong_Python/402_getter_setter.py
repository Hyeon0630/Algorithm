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
    
    def get_r(self):
        return self.__r
    
    def set_r(self, r):
        if r <= 0:
            raise TypeError("길이는 양의 숫자")
        else:
            self.__r = r
    
circle = Circle(10)
print("원의 둘레:", circle.circumference())
print("원의 넓이:", circle.area())

print()
print("# __r에 접근합니다.")
print(circle.get_r())

circle.set_r(2)

print()
print("# 반지름 변경 후")
print("원의 둘레:", circle.circumference())
print("원의 넓이:", circle.area())