import sys
input = sys.stdin.readline

s = list(input())
s.pop()
print(s)

def solution(s):
    result = []
    # start = 0, end = len(s) // 2
    # 인덱스 start, end를 두고 s[start:end] == s[end:2end-start]
    # 맞으면 result.append(2)
    # result.append(s[start:end])
    # 없으면 end -= 1
    # start == end이면 start += 1, end = len(s)-start // 2
    
    for start in range(len(s)-3):
        end = len(s)-start // 2
    return 0

print(solution(s))