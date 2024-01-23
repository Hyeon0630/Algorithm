def factorial(n):
    o = 1
    for i in range(1, n + 1):
        o *= i
    return o

for i in range(1, 6):
    j = str(i)
    print(j + "! =", factorial(i))
