def sum(start = 0, end = 100, step = 1):
    output = 0

    for i in range(start, end + 1, step):
        output += i

    return output

print("A.", sum(0, 100, 10))
print("B.", sum(end = 100))
print("c.", sum(end = 100, step = 2))