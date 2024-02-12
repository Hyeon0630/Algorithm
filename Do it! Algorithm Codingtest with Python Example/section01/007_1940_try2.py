# 시간 초과

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))

count = 0
num.sort()
s = 0
e = 1

while s != N-1:
    if (num[s] + num[e]) == M:
        count += 1
        s += 1
        e = s + 1
    elif e == (N-1):
        s += 1
        e = s + 1
    else:
        e += 1

print(count)