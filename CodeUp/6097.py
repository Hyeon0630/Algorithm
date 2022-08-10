h, w = input().split()
h = int(h)
w = int(w)
array = []
for i in range(h) : 
    array.append([])
    for j in  range(w) : 
        array[i].append(0)

n = int(input())
for i in range(n) :
    l, d, x, y = input().split()
    if int(d) == 1 : 
        for j in range(int(l)) : 
            array[int(x)+j-1][int(y)-1] = 1
    else : 
        for j in range(int(l)) : 
            array[int(x)-1][int(y)+j-1] = 1

for i in range(h) : 
    for j in range(w) : 
        print(array[i][j], end = ' ')
    print()