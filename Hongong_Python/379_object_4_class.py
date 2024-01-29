class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self. korean = korean
        self. math = math
        self. english = english
        self. science = science

    def sum(self):
        return self.korean + self.math + self.english + self.science
    
    def avg(self):
        return self.sum() / 4
    
    def string(self):
        return "{}\t{}\t{}".format(self.name, self.sum(), self.avg())
    
student = [
    Student("A", 87, 87, 88, 95),
    Student("B", 92, 87, 88, 95),
    Student("C", 76, 87, 88, 95),
    Student("D", 98, 87, 88, 95),
    Student("E", 95, 87, 88, 95),
    Student("F", 64, 87, 88, 95)
]

print("이름\t총점\t평균")
for i in student:
    print(i.string())