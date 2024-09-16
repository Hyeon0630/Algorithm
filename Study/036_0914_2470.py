import sys
input = sys.stdin.readline

N = int(input()) # 5
arr = sorted(list(map(int, input().split()))) # -2 4 -99 -1 98
# arr = [-99, -2, -1, 4, 98]

s, e = 0, N - 1 # 투포인터 s = 0, e = 4
result = [arr[s], arr[e]] # 출력할 값 result = [-99, 98]

tmp = abs(arr[s] + arr[e]) # 초기값 |-99 + 98| = |-1| = 1
while s < e:
    new = arr[s] + arr[e]
    if abs(new) < tmp:
        tmp = abs(new)
        result = [arr[s], arr[e]]

    if new >= 0: # arr[e]가 큼 -> e--
        e -= 1
    else: # arr[s]가 큼 -> s++
        s += 1

print(result[0], result[1])