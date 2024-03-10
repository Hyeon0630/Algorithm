import sys
input = sys.stdin.readline

N = int(input())
S = list()

for i in range(N):
    S.append(list(map(int, input().split())))

S.sort()

def Solution(s):
    # 반복문 돌며 index[]에 선택한 인덱스 기억 
    # end보다 크거나 같은 값 있으면 end에 [1] 저장 후 인덱스에 append
    # for 문 종료되면 index 에 있는 것을 s에서 제거
    # ans += 1
    # while문으로 감싸서 len(s) == 0되면 종료 
    
    ans = 0
    index = [0]
    while len(s) > 0:
        end = s[0][1]
        for i in range(len(s)):
            if s[i][0] >= end:
                end = s[i][1]
                index.append(i)
        ans += 1
        for i in reversed(index):
            del s[i]
            index.pop()
        index.append(0)
    return ans

answer = Solution(S)
print(answer)