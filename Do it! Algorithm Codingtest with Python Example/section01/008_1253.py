import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

p = N-1
e = N-2
s = 0
count = 0

A.sort()

while p > 1 and s < e:
    if A[p] == A[s] + A[e]:
        count += 1
        p -= 1
        e = p - 1
        s = 0
    elif A[p] < A[s] + A[e]:
        e -= 1
    elif A[p] > A[s] + A[e]:
        s += 1

print(count)