import sys
input = sys.stdin.readline

N, A = map(int, input().split())

room = [list(map(int, input().split())) for i in range(N)]
M = 0
mini = float("inf")

for i in room:
    if i[0] == 1:
        if i[2] % A == 0:
            M -= (i[2] // A - 1) * i[1]
        else:
            M -= (i[2] // A) * i[1]
        mini = min(M, mini)
    elif i[0] == 2:
        A += i[1]
        M += i[2]
        if M > 0 :
            M = 0

print(abs(mini) + 1)