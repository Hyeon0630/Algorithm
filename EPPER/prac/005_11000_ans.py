import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
lec = list(tuple(map(int, input().split())) for i in range(N))

def Solution(lec):
    lec.sort()
    tree = [-1]
    for s, e in lec:
        if tree[0] <= s:
            hq.heappop(tree)
        hq.heappush(tree, e)
    return len(tree)

print(Solution(lec))