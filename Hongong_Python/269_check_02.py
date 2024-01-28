numbers = list(range(1, 10 + 1))

print("# 홀수")
print(list(filter(lambda i: i % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만")
print(list(filter(lambda i: 3 <= i < 7, numbers)))
print()

print("# 제곱해서 50 미만")
print(list(filter(lambda i: i * i < 50, numbers)))