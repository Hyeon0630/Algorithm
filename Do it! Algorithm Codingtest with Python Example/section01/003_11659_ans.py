import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
temp = 0

for i in num:
    temp += i
    sum.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1])