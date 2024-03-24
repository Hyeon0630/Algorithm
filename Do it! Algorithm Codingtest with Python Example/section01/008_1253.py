import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = 0

s = 0
l = N - 2
c = N - 1

A.sort()

while(s < l and l >= 1 and s <= N - 3):
    temp = A[s] + A[l]
    if A[c] == temp:
        count += 1
        s = 0
        c -= 1
        l = c - 1
    elif A[c] < temp:
        l -= 1
    else:
        s += 1

if A[0] == A[1] == A[2]:
    count += 2
elif A[1] - A[0] in A:
    count += 1

print(count)

# for i in range(N, 2, -1):
#     for j in range(0, i):
#         if i-j in A:
#             count+=1
#             break


# p = N-1
# e = N-2
# s = 0 

# while p > 1 and s < e:
#     if A[p] == A[s] + A[e]:
#         count += 1
#         p -= 1
#         e = p - 1
#         s = 0
#     elif A[p] < A[s] + A[e]:
#         e -= 1
#     elif A[p] > A[s] + A[e]:
#         s += 1