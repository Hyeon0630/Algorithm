class Student():
    def study(self):
        print("공부를 합니다.")

class Teacher():
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for i in classroom:
    if isinstance(i, Student):
        i.study()
    elif isinstance(i, Teacher):
        i.teach()