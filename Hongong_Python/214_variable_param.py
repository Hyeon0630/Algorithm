# 가변 매개변수 함수
def repeat(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

repeat(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")