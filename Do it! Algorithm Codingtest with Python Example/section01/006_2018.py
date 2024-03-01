import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 1
sum = 1
count = 1

while end != N:
    if sum == N:
        count += 1
        sum -= start
        start += 1
    elif sum > N:
        sum -= start
        start += 1
    elif sum < N:
        end += 1
        sum += end

print(count)