m = []
for i in range(10) : 
    m.append([])
    for j in range(10) : 
        m[i].append(0)

for i in range(10) : 
    a = input().split()
    for j in range(10) : 
        m[i][j] = int(a[j])

x = 1
y = 1

while True : 
    if m[x][y] == 0 : 
        m[x][y] = 9
    elif m[x][y] == 2 : 
        m[x][y] = 9
        break

    if (m[x+1][y] == 1 and m[x][y+1] == 1) or (x == 8 and y == 8) : 
        break
    
    if m[x][y+1] != 1 : 
        y += 1
    elif m[x+1][y] != 1 : 
        x += 1

for i  in range(10) : 
    for j in range(10) :
        print(m[i][j], end =' ')
    print()