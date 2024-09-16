import sys
input = sys.stdin.readline
# https://infinitt.tistory.com/229
# 버블소트 -> 매 회차 제일 큰 값이 맨 뒤로
# 10 1 5 2 3
# 1 5 2 3 10 (1회)
# 1 2 3 5 10 (2회)
# 한 숫자 기준으로 얼마나 앞으로 이동했나
# 횟수 + 1

N = int(input()) # N = 5
A = [] 
result = [] # 출력은 max(result)

for i in range(N):
    tmp = int(input())
    A.append((tmp, i))
# A = [(10, 0), (1, 1), (5, 2), (2, 3), (3, 4)]

SA = sorted(A) # SA = [(1, 1), (2, 3), (3, 4), (5, 2), (10, 0)]
for i in range(N):
    result.append(SA[i][1] - A[i][1]) 
    # result = [1, 2, 2, -1, -4]

print(max(result) + 1) # 3