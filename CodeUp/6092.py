n = int(input())
input = input().split()

for i in range(n) : 
    input[i] = int(input[i])

array = []
for i in range(24) :
    array.append(0)

for i in range(n) : 
    array[input[i]] += 1

for i in range(1, 24) : 
    print(array[i], end = ' ')