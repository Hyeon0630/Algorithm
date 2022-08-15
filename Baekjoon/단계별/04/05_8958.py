n = int(input())
a=[]
for i in range(n) : 
    a.append([])
    a[i].append(input())
cnt = 0
temp = 0
for i in range(n) : 
    for j in range(len(a[i])) :
        if a[i][j] == 'O' : 
            temp += 1
        elif a[i][j] == 'X' :
            for k in range(1, temp+1) : 
                cnt += k
            temp = 0
        if a[i][len(a[i])-1] == 'O' :
            for k in range(1, temp+1) : 
                cnt += k
    print(cnt)
