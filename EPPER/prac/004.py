import sys
input = sys.stdin.readline

s = list(input())
s.pop()

# 일단 window 길이 8>4~2, 9 -> 9//2~2

def solution(s):
    result = []
    window = len(s)//2
    while(window >= 2):
        # 9 이면 4, 0~8 5678 len(s) = 9 - 4
        # window가 4이면 for i in range(0, len(s), 1)
        for i in range(0, len(s)-window+1):
            check = s[i:i+window]
            uncheck = s[i+window:]
            cnt = 1
            while(1):
                start = i+window
                end = i+2*window
                if check in s[start:end]:
                    cnt += 1
                    start += window
                    end += window
                else:
                    break
            if cnt >= 2:
                result.append(cnt)
                result.append(check)
                result.append(uncheck)
                break
                # 재귀함수
            else:
                window -= 1

    # start = 0, end = len(s) // 2
    # 인덱스 start, end를 두고 s[start:end] == s[end:2end-start]
    # 맞으면 result.append(2)
    # result.append(s[start:end])
    # 없으면 end -= 1
    # start == end이면 start += 1, end = len(s)-start // 2
    
    return len(result)

print(solution(s))