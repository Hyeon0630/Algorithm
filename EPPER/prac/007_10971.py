import sys
input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for i in range(N))

INF = 1e8
ans = INF
visited = []
matrix = []

def backt(n, cnt, curc, cost):
    global ans, visited, matrix
    if cost >= ans:
        return
    
    if cnt == n:
        if matrix[curc][0] != 0:
            ans = min(ans, cost + matrix[curc][0])
        return
    
    for i in range(n):
        if matrix[curc][i] and visited[i] == False:
            visited[i] = True
            backt(n, cnt + 1, i, cost + matrix[curc][i])
            visited[i] = False

def solution(n, cost):
    global ans, visited, matrix
    visited = [False] * n
    visited[0] = True
    matrix = cost
    backt(n, 1, 0, 0)    
    return ans

print(solution(N, W))