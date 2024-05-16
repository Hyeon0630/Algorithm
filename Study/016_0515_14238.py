# 오늘을 기준으로 전날, 전전날 정보 필요
# 오늘 들어오는게 C일 경우 전날 전전날이 C가 아님
# 오늘 들어오는게 B일 경우 전날이 B가 아님

import sys
input = sys.stdin.readline

s = list(input().rstrip())
arr = [0 for i in range(len(s))]
a, b, c = 0, 0, 0
q, w, e = 0, 0, 0

for i in s:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'C':
        c += 1

while c > 0 and q < len(s):
    # if arr[q] == 'D':
    arr[q] = 'C'
    q += 3 # 0, 1, 2, 3
    c -= 1

if q > 0:
    w, e = 1, 1

while b > 0 and w < len(s):
    arr[w] = 'B'
    w += 2 # 1, 2, 3
    b -= 1

while a > 0 and e < len(s):
    if arr[e] == 0:
        arr[e] = 'A'
        a -= 1
    e += 1

if 0 in arr:
    a, b, c = 0, 0, 0
    q, w, e = 0, 0, 0

    for i in s:
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
    
    arr = [0 for i in range(len(s))]
    
    while b > 0 and w < len(s):
        arr[w] = 'B'
        w += 2 # 1, 2, 3
        b -= 1
        
    if w > 0:
        q, e = 1, 1

    while c > 0 and q < len(s):
        # if arr[q] == 'D':
        arr[q] = 'C'
        q += 3 # 0, 1, 2, 3
        c -= 1

    while a > 0 and e < len(s):
        if arr[e] == 0:
            arr[e] = 'A'
            a -= 1
        e += 1

if 0 in arr:
    print(-1)
else:
    print("".join(reversed(arr)))