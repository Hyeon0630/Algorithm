# 1253, 1021

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
po = list(map(int, input().split()))

def solution(n, m, p):
    ans = 0
    q = [i+1 for i in range(0, n)]
    c = 0
    # 0
    # p의 원소 i-1이 0과 가까운지
    # 예를 들어 
    # 12345678910
    # 2를 뽑고싶으면 거리 계산 i-1에서 현위지 1 빼기
    #  9번
    while(len(p) == 0):
        for i in p:
            a = i-1-c
            b = n-a
            if a < b:
                
            ans += min(a, b)
            
    q[m-1]
    return ans

print(solution(N, M, po))