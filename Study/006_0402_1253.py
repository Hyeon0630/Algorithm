import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = 0

A.sort()

# 투포인터
s = 0
l = N - 1
search = 0

for i in range(N):
    search = A[i]
    s = 0
    l = N - 1
    while(s < l):
        temp = A[s] + A[l]
        if temp == search:
            if s == i:
                s += 1
            elif l == i:
                l -= 1
            else:
                count += 1
                break
        elif temp < search: # 작을 경우
            s += 1
        else: # 클 경우
            l -= 1

print(count)