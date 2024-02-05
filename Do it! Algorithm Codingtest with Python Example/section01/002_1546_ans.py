N = int(input())
s = list(map(int, input().split()))
m = max(s)
sum = sum(s)

print(sum / m * 100 / N)