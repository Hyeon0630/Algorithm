import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
d = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])

def solution(m, d, dq):
    ans = 0
    for i in range(0, m):
        key = d[i]
        while(True):
            if dq[0] == key:
                dq.popleft()
                break
            else:
                if dq.index(key) <= len(dq)//2:
                    while(dq[0] != key):
                        ans += 1
                        dq.append(dq.popleft())
                else:
                    while(dq[0] != key):
                        ans += 1
                        dq.appendleft(dq.pop())
    return ans

print(solution(M, d, dq))