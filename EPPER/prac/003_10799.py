import sys
input = sys.stdin.readline

arr = list(input())
arr.pop()

def solution(arr):
    answer = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == "(":
            cnt += 1
        else:
            cnt -= 1
            if arr[i-1] == "(":
                answer += cnt
            else:
                answer += 1
    return answer

ans = solution(arr)
print(ans)