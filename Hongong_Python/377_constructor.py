class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self. korean = korean
        self. math = math
        self. english = english
        self. science = science

student = [
    Student("A", 87, 87, 88, 95),
    Student("B", 92, 87, 88, 95),
    Student("C", 76, 87, 88, 95),
    Student("D", 98, 87, 88, 95),
    Student("E", 95, 87, 88, 95),
    Student("F", 64, 87, 88, 95)
]

print(student[0].name)
print(student[0].korean)
print(student[0].math)
print(student[0].english)
print(student[0].science)