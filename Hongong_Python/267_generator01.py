def test():
    print("A지점 통과")
    yield 1
    
    print("B지점 통과")
    yield 2

    print("C지점 통과")
    yield 3

output = test()

print("D지점 통과")
a = next(output)
print(a)

print("E지점 통과")
b = next(output)
print(b)

print("F지점 통과")
c = next(output)
print(c)

next(output)