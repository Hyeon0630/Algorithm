def sum(start, end):
    sum = 0

    for i in range(start, end + 1):
        sum += i
    
    return sum

print("0 to 100:", sum(0, 100))
print("0 to 1000:", sum(0, 1000))
print("50 to 100:", sum(50, 100))
print("500 to 1000:", sum(500, 1000))