a = []
for i in range(10) : 
    a.append([])
    for j in range(10) : 
        a[i].append(0)

for i in range(10) : 
    input = input().split()
    for j in range(10) : 
        a[i+1][j+1] = int(input[j])

x = 2
y = 2

while True : 
    if a[x][y] == 0 : 
        a[x][y] = 9
    elif a[x][y] == 2 :
        a[x][y] = 9
        break

    if((a[x][y+1] == 1 and a[x+1][y] == 1) or (x == 8 and y == 8)) : 
        break
    
    if a[x][y+1] != 1 : 
        y += 1
    elif a[x+1][y] != 1 : 
        x += 1

for i in range(10) : 
    for j in range(10) : 
        print(a[i][j], end = ' ')
print()
