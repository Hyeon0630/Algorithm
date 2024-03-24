import sys
input = sys.stdin.readline

def solution(n, record):
    ans = ""
    pan = ["?"]*n
    p = 0

    for i in range(len(record)):
        p += int(record[i][0])
        c = str(record[i][1])
        if pan[p%n] != '?' and pan[p%n] != c:
            ans = "!"
        elif c in pan and pan[p%n] != c:
            ans = "!"
        else:
            pan[p%n] = c
        
        if ans != "!":
            f = reversed(pan[0:p%n + 1])
            r = reversed(pan[p%n + 1:n])
            ans = "".join(f)+"".join(r)

    return ans

n, k = map(int, input().split())
record = [input().split() for _ in range(k)]
    
print(solution(n, record))