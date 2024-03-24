import sys
input = sys.stdin.readline

s = list(input())
s.pop()

def cntl(arr, unit):
    nlength = len(unit)
    unitarr = ""
    cnt = 1

    lstart = 0
    rstart = unit

    while rstart <= len(unit):
        comparr = arr[lstart:rstart]

        if unitarr == comparr:
            cnt += 1
        else:
            if cnt > 1:
                nlength += len(str(cnt))
                nlength -= (cnt - 1) * unit
            unitarr = comparr
            cnt = 1

        lstart += unit
        rstart += unit

        if cnt > 1:
                nlength += len(str(cnt))
                nlength -= (cnt - 1) * unit

    return nlength

def solution(s):
    ans = len(s)
    for i in range(1, len(s)//2+1):
        ans = min(ans, cntl(s, i))
    
    return ans

print(solution(s))