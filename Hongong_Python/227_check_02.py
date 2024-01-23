def mul(*values):
    o = 1

    for i in values:
        o = o * i
    
    return o

print(mul(5, 7, 9, 10))