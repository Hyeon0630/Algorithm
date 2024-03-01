import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pan = list()
s = 0
q = 0

for i in range(N):
    pan.append("?")

for i in range(K):
    a, b = input().split()
    a = int(a)
    b = str(b)
    s += a
    if pan[s % N] != "?" and pan[s % N] != b:
        q = 1
    elif b in pan and pan[s % N] != b:
        q = 1
    else: 
        pan[s % N] = b

if q == 0:
    f = reversed(pan[0:s % N + 1])
    r = reversed(pan[s % N + 1:N])

    print(*f, *r, sep="")
else:
    print("!")