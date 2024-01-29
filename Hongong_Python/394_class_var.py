class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self. korean = korean
        self. math = math
        self. english = english
        self. science = science
        
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

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

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))