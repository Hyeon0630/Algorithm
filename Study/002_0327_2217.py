import sys
input = sys.stdin.readline

N = int(input())
W = []
for i in range(N):
    W.append(int(input()))
W.sort()

def solution(n, w):
    ans = []
    for i in range(len(w)):
        ans.append(w[i]*(len(w)-i))
    return max(ans)

print(solution(N, W))