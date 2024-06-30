import sys
input = sys.stdin.readline

stuff = []
N, K = map(int, input().split())
dp = [0 for i in range(K+1)]

for i in range(N):
    stuff.append(list(map(int, input().split())))

for i in stuff:
    for j in range(K, i[0] - 1, -1):
        dp[j] = max(dp[j], dp[j - i[0]] + i[1])

print(dp[-1])