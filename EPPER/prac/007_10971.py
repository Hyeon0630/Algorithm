import sys
input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for i in range(N))

INF = 1e8
ans = INF
visited = []
matrix = []

def backt(n, cnt, curcity, cost):
    global ans, visited, matrix
    if cost >= ans:
        return
    if cnt == n:
        if matrix[curcity][0] != 0:
            ans = min(ans, cost + matrix[curcity][0])
        return
    for i in range(0, n):
        if matrix[curcity][i] and visited[i] == 0:
            visited[i] = True
            backt(n, cnt+1, i, cost+matrix[curcity][i])
            visited[i] = False


def solution(n, cost):
    global ans, visited, matrix

    visited = [False]*n
    visited[0] = True
    matrix = cost
    
    backt(n, 1, 0, 0)

    return ans

print(solution(N, W))