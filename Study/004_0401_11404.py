import sys
input = sys.stdin.readline

INF = int(1e9) # min 비교 위해서 최댓값으로 초기화

n = int(input()) # 도시
m = int(input()) # 버스

ans = [[INF]*(n+1) for i in range(n+1)] # 그래프
for i in range(1, n+1):
    ans[i][i] = 0 # 자기 자신 0으로

for i in range(m):
    a,b,c = map(int, input().split())
    ans[a][b] = min(ans[a][b], c)

# 두 경로의 합이 더 적은 비용일 경우를 고려
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            ans[j][k] = min(ans[j][k], ans[j][i]+ans[i][k])

# 출력 - 0인 것 처리 필요
for i in range(1, n+1):
    for j in range(1, n+1):
        if (ans[i][j] == INF):
            print(0, end = " ")
        else: 
            print(ans[i][j], end = " ")
    print()