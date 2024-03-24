import sys
input = sys.stdin.readline

s = list(input())
s.pop()

def cntl(arr, unit):
    length = len(arr)
    nlength = length
    cnt = 1
    p = ""

    l = 0
    r = unit

    while r <= length:
        c = arr[l:r]
        if p == c:
            cnt += 1
        else:
            if cnt > 1:
                nlength += len(str(cnt))
                nlength -= unit * (cnt - 1)
            cnt = 1
            p = c

        l += unit
        r += unit

    if cnt > 1:
        nlength += len(str(cnt))
        nlength -= unit * (cnt - 1)
        
    return nlength


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):        
        answer = min(answer, cntl(s, i))
    return answer

print(solution(s))