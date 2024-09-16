import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

result = 0

while max(B) > 0:
    # 2로 나누어 떨어지지 않으면 1을 빼고 나누어 떨어지면 // 2
    for i in range(N):
        if B[i] % 2 != 0:
            B[i] -= 1
            result += 1

    if max(B) > 0: # 모두 0이 되면 멈추도록
        for i in range(N):
            B[i] //= 2
        result += 1

print(result)