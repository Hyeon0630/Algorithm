N = int(input())
s = list(map(int, input().split()))
sum = float(0)

for i in s:
    sum += i/max(s)*100

print(float(sum/N))