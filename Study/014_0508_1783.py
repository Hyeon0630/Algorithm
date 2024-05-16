import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0

if n == 1:
    ans = 1
elif n == 2:
    if 1 <= m and m <= 6:
        ans = (m + 1) // 2
    elif m >= 7:
        ans = 4
elif n >= 3:
    if 1 <= m and m <= 3:
        ans = m
    elif 4 <= m and m <= 6:
        ans = 4
    elif m >= 7:
        ans = m - 2

print(ans)