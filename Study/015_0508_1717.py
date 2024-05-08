import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set = [i for i in range(0, n+1)] 
# {0}, {1}, ... , {n}
# 1이 든 집합은 set[1]로 확인 -> set[1] = 1이면 [1]인거고 set[1] = 7이면 [1, 7]

# find
def find(p):
    if set[p] != p:
        set[p] = find(set[p])
    return set[p]

# union
def union(p, q):
    p = find(p)
    q = find(q)
    if find(p) > find(q):
        set[q] = p 
    else:
        set[p] = q

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")