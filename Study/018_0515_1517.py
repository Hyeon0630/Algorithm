import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def bubblesort(arr):
    ans = 0
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                ans += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return ans

print(bubblesort(A))