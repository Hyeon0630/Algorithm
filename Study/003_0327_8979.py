import sys
input = sys.stdin.readline

N, M = map(int, input().split())
medal = [list(map(int, input().split())) for i in range(N)]

def solution(n, k, m):
    rank = 1
    m.sort()
    for i in range(n):
        if m[k-1][1] < m[i][1]:
            rank += 1
        elif  m[k-1][1] == m[i][1]:
            if m[k-1][2] < m[i][2]:
                rank += 1
            elif m[k-1][2] == m[i][2]:
                if m[k-1][3] < m[i][3]:
                    rank += 1

    return rank

print(solution(N, M, medal))