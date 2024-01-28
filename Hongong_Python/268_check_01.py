numbers = [1, 2, 3, 4, 5, 6]

# print("::".join(str(numbers).split(", ")))

print("::".join(map(str, numbers)))

floats = [1.1, 2.2, 3.3, 4.4]

print(list(map(int, floats)))