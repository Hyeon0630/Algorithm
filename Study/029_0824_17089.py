import sys
input = sys.stdin.readline

N, M = map(int, input().split())
f = [[] for i in range(N + 1)]
result = M

for i in range(M):
    a, b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)

for i in range(1, N+1):
    if len(f[i]) >= 2:
        for j in f[i]:
            for k in f[j]:
                if k in f[i]:
                    result = min(result, len(f[i]) + len(f[j]) + len(f[k]) - 6)

if result < M:
    print(result)
else:
    print(-1)