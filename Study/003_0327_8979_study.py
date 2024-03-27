import sys
input = sys.stdin.readline

N, M = map(int, input().split())
medal = [list(map(int, input().split())) for i in range(N)]


def solution(n, k, m):
    m.sort(key = lambda x: (-x[1],-x[2],-x[3]))
    rank = 1
    temp = 0
    tempck = False

    if m[0][0] == k:
        return rank
    
    for i in range(1, n):
        rank += 1
        if m[i][1:] == m[i-1][1:]:
            temp += 1
            tempck = True
        else:
            temp = 0
            tempck = False
        if m[i][0]==k:
            break
    
    if(tempck):
        rank = rank-temp
    return rank

print(solution(N, M, medal))