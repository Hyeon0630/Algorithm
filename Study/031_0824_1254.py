import sys
input = sys.stdin.readline

S = input().strip()

result = len(S) * 2 - 1

for i in range(len(S)):
    s = S[i:]
    if s == s[::-1]:
        print(s, s[::-1])
        result = min(result, len(S) + i)

print(result)