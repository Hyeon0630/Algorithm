import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

sum_p = [(N+1) * [0] for i in range(N+1)]

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += arr[i-1][j-1]
        sum_p[i][j] = sum_p[i - 1][j] + temp

for i in range(M):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    print(sum_p[x_2][y_2] - sum_p[x_1 - 1][y_2] - sum_p[x_2][y_1 - 1] + sum_p[x_1 - 1][y_1 - 1])