N = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0

for i in range(1, N+1):
    result += sum(p[0:i])

print(result)