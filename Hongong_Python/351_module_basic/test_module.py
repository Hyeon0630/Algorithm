import math as m

PI = m.pi

def input_radius():
    output = input("숫자 입력 > ")
    return float(output)

def circumference(radius):
    return PI*2*radius

def area(radius):
    return PI*radius*radius