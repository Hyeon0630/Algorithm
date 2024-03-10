import sys
input = sys.stdin.readline
MOD = 1000000007

n = int(input())

def solution(n):
    answer = 0
    partsum = [0, 3, 11]
    if n % 2 != 0:
        answer = 0
    else:
        for i in range(6, n + 1, 2):
            partsum.append((partsum[i//2 - 1]*4 - partsum[i//2 - 2]) % MOD)
        answer = partsum[n//2]
    return answer

print(solution(n))