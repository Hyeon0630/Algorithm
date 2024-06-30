import sys
input = sys.stdin.readline

# 밑면이 0이 아닌 것의 개수를 카운트
# 앞면 뒷면은 행 max를 각 행마다 구한 뒤 더함
# 오른면 왼면은 열 max를 각 행마다 구한 뒤 더함

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for j in range(n)]

result = 0
a = n*m
b = 0
c = 0

for i in range(n):
    for j in range(m):
        if j == 0:
            b += paper[i][j]
        else:
            if paper[i][j] > paper[i][j-1]:
                b += paper[i][j] - paper[i][j-1]

for j in range(m):
    for i in range(n):
        if i == 0:
            c += paper[i][j]
        else:
            if paper[i][j] > paper[i-1][j]:
                c += paper[i][j] - paper[i-1][j]

result = 2*(a+b+c)
print(result)