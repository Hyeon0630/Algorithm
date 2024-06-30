import sys
input = sys.stdin.readline

d, t = map(str, input().split())
x, y = map(int, input().split())
d = int(d)
s = list(map(int, t))
ans = []

xx = 0
yy = 0

for k in range(d):
    if s[k] == 1:
        xx += (2**len(s))//(2**(k+1))
    elif s[k] == 3:
        yy += (2**len(s))//(2**(k+1))
    elif s[k] == 4:
        xx += (2**len(s))//(2**(k+1))
        yy += (2**len(s))//(2**(k+1))

xx += x
yy -= y

if xx < 0 or xx >= 2**len(s) or yy < 0 or yy >= 2**len(s):
    print(-1)
else:
    for k in range(d):
        if xx >= (2**(len(s)-k-1)) and yy < (2**(len(s)-k-1)):
            ans.append(1)
            xx -= (2**(len(s)-k-1))
        elif xx < (2**(len(s)-k-1)) and yy < (2**(len(s)-k-1)):
            ans.append(2)
        elif xx < (2**(len(s)-k-1)) and yy >= (2**(len(s)-k-1)):
            ans.append(3)
            yy -= (2**(len(s)-k-1))
        else:
            ans.append(4)
            xx -= (2**(len(s)-k-1))
            yy -= (2**(len(s)-k-1))
    print(*ans, sep="")