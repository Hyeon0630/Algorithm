list_a = [0, 1, 2, 3, 4, 5, 6]

print("list_a의 요소 하나씩 삭제하기")
print("\n", list_a)

del list_a[1]
print("\ndel list[1] : ", list_a)

list_a.pop(2)
print("\npop(2) : ", list_a)

list_a.pop()
print("\npop() : ", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]

print("\n\nlist_a의 요소 하나씩 삭제하기")
print("\n", list_b)

del list_b[1:3] # 인덱스 3은 포함하지 않음
print("\ndel list[1:3] : ", list_b)

del list_b[:2] # 인덱스 2은 포함하지 않음
print("\ndel list[:2] : ", list_b)

del list_b[2:] # 인덱스 2를 포함
print("\ndel list[2:] : ", list_b)