N = int(input())
array = []

for i in range(N):
    n = int(input())
    if n not in array:
        array.append(n)

for i in range(len(array) - 1, 0, -1):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j+1] = array[j+1], array[j]

for i in array:
    print(i)