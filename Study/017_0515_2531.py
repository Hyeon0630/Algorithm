import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
s = [0] * N
ans = 0

# 초밥
for i in range(N):
    s[i] = int(input())

# s[0:k] 늘려주기
s.extend(s[0:k])

for i in range(N):
    temp = set(s[i:i+k]) # set 함수로 중복 요소 제거

    if c not in temp:
        if len(temp) + 1 > ans:
            ans = len(temp) + 1
    else:
        if len(temp) > ans:
            ans = len(temp)

print(ans)