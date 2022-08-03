# CodeUp Python 기초 100제 #6075번
# print문 정리(sep, end, format 등)

from os import sep

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print("< sep & end 1 >")
print(a, b, c)

print("\n\n< 1 - sep >")
print(a, b, c, sep=':')
print(a, b, c, sep='-')

print("\n\n< 1 - end >")
print(a, b, c, end=':')
print("\n")
print(a, b, c, end='-')


print("\n\n< sep & end 2 >")
for i in range(1, 6) : 
    print(i)

print("\n\n< 2 - sep >")
for i in range(1, 6) : 
    print(i, sep = " ")
print("\n")
for i in range(1, 6) : 
    print(i, sep = ":")
print("\n")
for i in range(1, 6) : 
    print(i, sep = "-")
    
print("\n\n< 2 - end >")
for i in range(1, 6) : 
    print(i, end = " ")
print("\n")
for i in range(1, 6) : 
    print(i, end = ":")
print("\n")
for i in range(1, 6) : 
    print(i, end = "-")


print("\n\n< format >")
day = 3
str = "수"
print("오늘은 2022년 8월 ",day, "일이고 ", str, "요일입니다")

print("\n\n< format - % >")
# %d : 정수
# %o : 8진수
# %x : 16진수
# %f : 실수
# %s : 문자열
print("오늘은 2022년 8월 %d일이고 %s요일입니다" %(day, str))

print("\n\n< format - format() >")
print("오늘은 2022년 8월 {0}일이고 {1}요일입니다".format(day, str))

print("\n\n< format - f-string >")
print(f"오늘은 2022년 8월 {day}일이고 {str}요일입니다")