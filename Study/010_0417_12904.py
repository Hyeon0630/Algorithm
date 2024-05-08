import sys
input = sys.stdin.readline

S = list(input().strip("\n"))
T = list(input().strip("\n"))

# 1 / 0 print를 위해 상태 확인 변수
ans = 0

while(len(T) >= len(S)):
    l = T.pop()
    if l == "B":
        T.reverse()
    if T == S:
        ans = 1
        break

if ans == 1:
    print("1")
else:
    print("0")