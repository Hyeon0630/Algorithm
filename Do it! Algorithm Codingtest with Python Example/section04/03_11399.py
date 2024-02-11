N = int(input())
p = [0]*N
p = input().split()

p = list(reversed(sorted(p)))

result = 0
for i in range(1, N+1):
    a = int(p[i-1])
    result += int(i * a)

print(result)