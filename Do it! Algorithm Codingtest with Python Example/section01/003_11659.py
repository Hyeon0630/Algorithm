N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]*(N+1)
for i in range(N):
    sum[i+1] = sum[i] + num[i]

for i in range(M):
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1])