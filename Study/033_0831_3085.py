import sys
input = sys.stdin.readline

def countm(a):
    r = 1
    for i in range(N):
        # 행
        t = 1
        for j in range(1, N):
            if a[j][i] == a[j-1][i]:
                t += 1
            else:
                t = 1
            r = max(r, t)
        # 열
        t = 1 
        for j in range(1, N):
            if a[i][j] == a[i][j-1]:
                t += 1
            else:
                t = 1
            r = max(r, t)
    return r

N = int(input())
candy = list(list(input().strip()) for i in range(N))
result = 0

for i in range(N):
    for j in range(N):
        if i+1 < N: # 행 
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            temp = countm(candy)
            result = max(result, temp)
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        if j+1 < N: # 열
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] 
            temp = countm(candy)
            result = max(result, temp)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] 

print(result)