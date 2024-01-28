def test():
    print("안녕")
    yield "test"

print("A지점 통과")
test()

print("B지점 통과")
print(list(test()))