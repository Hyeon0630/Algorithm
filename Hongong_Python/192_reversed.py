list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print(list_reversed)
print(list(list_reversed))
print()

for i in list_reversed:
    print("-", i)

# 제너레이터
print()
print("# reversed() 함수")
print(list(reversed(list_a))) # reversed(list_a)만 넣으면 X
print()

for i in reversed(list_a):
    print("-", i)