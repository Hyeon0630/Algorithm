import sys
input = sys.stdin.readline
N, K = map(int, input().split())
m = [list(map(int, input().split())) for i in range(N)]

def check(a, me, color, m):
    if m[a][color] > m[me-1][color]:
        return int(1)
    elif m[a][color] == m[me-1][color] and a != me-1 and color >= 3:
        check(a, me, color+1, m)

def solution(n, k, m):
    ans = 0
    for i in range(n):
        ans += check(i, k, 1, m)
    return ans

print(solution(N, K, m))