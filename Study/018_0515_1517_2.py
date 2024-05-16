# 버블소트로는 시간초과라서 합병정렬 사용
# 버블소트는 내가 뒤에 것보다클 때 ans를 증가
# 따라서 병합정렬을 하면서 이런 경우레는 ans 증가

# 
# 8, 3, 1, 4
# 8, 3 // 1, 4
# 8 // 3 //// 1 // 4
# 3, 8 // 1, 4
# 1, 3, 4, 8


import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 답
ans = 0

def merge(l, r):
    i, j = 0, 0
    arr = []
    global ans

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else: # l[i] > r[j]
            arr.append(r[j])
            j += 1
            # len(l) - i개의 값들은 모두 r[j] 오른쪽으로 이동하는 것이나 마찬가지
            ans += len(l) - i
    
    if i == len(l):
        arr.extend(r[j:])
    else:
        arr.extend(l[i:])

    return arr

def mergesort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    larr = mergesort(arr[:mid])
    rarr = mergesort(arr[mid:])

    return merge(larr, rarr)

A = mergesort(A)
print(ans)