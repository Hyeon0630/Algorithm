import sys
input = sys.stdin.readline

p = list(map(int, input().split()))

P = [[0 for i in range(8)] for j in range(8)]
Pch = 0

for i in range(8):
    for j in range(i + 1, 8):
        P[i][j] = p[Pch]
        P[j][i] = 100 - P[i][j]
        Pch += 1

print(P)

result = [[0 for i in range(8)] for j in range(3)]

# print(result)

for i in range(4):
    result[0][2*i] = P[2*i][2*i+1]
    result[0][2*i + 1] = P[2*i+1][2*i]

# print(result[0])    

for j in range(4):
    if j % 2 == 0: # 0, 1, 4, 5인 경우
        result[1][2*j] = result[0][2*j]*(result[0][2*j+2]*P[2*j][2*j+2] + result[0][2*j+3]*P[2*j][2*j+3])
        result[1][2*j+1] = result[0][2*j+1]*(result[0][2*j+2]*P[2*j+1][2*j+2] + result[0][2*j+3]*P[2*j+1][2*j+3])
    else: # 2, 3, 6, 7인 경우
        result[1][2*j] = result[0][2*j]*(result[0][2*j-2]*P[2*j][2*j-2] + result[0][2*j-1]*P[2*j][2*j-1])
        result[1][2*j+1] = result[0][2*j+1]*(result[0][2*j-2]*P[2*j+1][2*j-2] + result[0][2*j-1]*P[2*j+1][2*j-1])

print(result[1])

for k in range(4):
    if k < 2: # 0, 1, 2, 3인 경우
        result[2][2*k] = result[1][2*k]*(result[1][4]*P[2*k][4] + result[1][5]*P[2*k][5] + result[1][6]*P[2*k][6] + result[1][7]*P[2*k][7])
        result[2][2*k+1] = result[1][2*k+1]*(result[1][4]*P[2*k+1][4] + result[1][5]*P[2*k+1][5] + result[1][6]*P[2*k+1][6] + result[1][7]*P[2*k+1][7])
    else: # 4, 5, 6, 7인 경우
        result[2][2*k] = result[1][2*k]*(result[1][0]*P[2*k][0] + result[1][1]*P[2*k][1] + result[1][2]*P[2*k][2] + result[1][3]*P[2*k][3])
        result[2][2*k+1] = result[1][2*k+1]*(result[1][0]*P[2*k+1][0] + result[1][1]*P[2*k+1][1] + result[1][2]*P[2*k+1][2] + result[1][3]*P[2*k+1][3])

for i in range(8):
    result[2][i] /= 100000000000000

print(*result[2])