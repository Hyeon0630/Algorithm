import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))

num.sort()

count = 0
s = 0
e = N - 1

while s < e:
    if (num[s] + num[e]) == M:
        count += 1
        s += 1
        e -= 1
    elif (num[s] + num[e]) > M:
        e -= 1
    elif (num[s] + num[e]) < M:
        s += 1

print(count)