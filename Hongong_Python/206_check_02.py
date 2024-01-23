# 2진수
b = "{:b}".format(10)
b_t = int(b, 2)

# 8진수
o = "{:o}".format(10)
o_t = int(o, 8)

# 16진수
x = "{:x}".format(10)
x_t = int(x, 16)

# count()
print(int("안녕안뇽하세요".count("안")))

# 문제

sum = 0

for i in range(1, 101):
    b_p = "{:b}".format(i)
    if b_p.count("0") == 1:
        print("{} : {}".format(i, b_p))
        sum += i

print("합계 :", sum)
