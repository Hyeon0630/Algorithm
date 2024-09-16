import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    print(start, end = " ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)