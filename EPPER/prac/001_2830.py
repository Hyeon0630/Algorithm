import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pan = list()

for i in range(N):
    pan.append("?")

def solution():
    answer = ""
    s = 0

    for i in range(K):
        a, b = input().split()
        a = int(a)
        b = str(b)
        s += a
        if pan[s % N] != "?" and pan[s % N] != b:
            answer = "!"
        elif b in pan and pan[s % N] != b:
            answer = "!"
        else: 
            pan[s % N] = b
        
        if answer != "!":
            f = reversed(pan[0:s % N + 1])
            r = reversed(pan[s % N + 1:N])
            answer = "".join(f)+"".join(r)

    return answer

ans = solution()
print(ans)