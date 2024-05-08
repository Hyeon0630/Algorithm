import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.sort()

ans = 1
for i in array:
    if ans < i:
        break
    ans += i

print(ans)