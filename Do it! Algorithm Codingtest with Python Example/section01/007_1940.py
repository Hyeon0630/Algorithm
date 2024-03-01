import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))

count = 0
e = []

for i in num:
    if i not in e and (M - i) in num:
        count += 1
        e.append(M - i)

print(count)