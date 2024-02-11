import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0] * N
sum[0] = arr[0]
count = 0
r = [0] * M

for i in range(1, N):
    sum[i] = sum[i - 1] + arr[i]

for i in range(N):
    sum[i] %= M
    if sum[i] == 0:
        count += 1
    r[sum[i]] += 1

for i in range(M):
    if r[i] > 1:
        count += (r[i] * (r[i] - 1) // 2)

print(count)