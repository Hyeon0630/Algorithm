import sys
input = sys.stdin.readline

s = list(input().rstrip())
length = len(s)

answer = [''] * length
A, B, C = 0, 1, 2
    
cnt = [s.count(word) for word in ('A', 'B', 'C')]

dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]

# parameter - 현재까지 쓴 A, B, C 개수, 전과 전전의 선택을 나타내는 prev
def dfs(a, b, c, prev):

    # parameter a, b, c의 개수 == cnt이면 답 출력
    if [a, b, c] == cnt:
        print(''.join(answer))
        exit(0)

		# 이미 방문했다면 dp[a][b][c][prev[0]][prev[1]] == True일테니 False
    if dp[a][b][c][prev[0]][prev[1]]:
        return False

		# 방문하지 않았다면 방문 상태 dp에 True로 기록
    dp[a][b][c][prev[0]][prev[1]] = True

    # A를 하나 쓸 수 있을 때
    if a + 1 <= cnt[A]: # 0 이었는데 1로 늘려도 개수 범위 내임
        answer[a + b + c] = 'A' # 답 배열에 A 추가
        if dfs(a + 1, b, c, [prev[1], A]):
            return True
    # B를 하나 쓸 수 있을 때
    if b + 1 <= cnt[B]:
        answer[a + b + c] = 'B'
        # 전 날 B가 아닌 다른 것 선택
        if prev[1] != B:
            if dfs(a, b + 1, c, [prev[1], B]):
                return True
    # C를 하나 쓸 수 있을 때
    if c + 1 <= cnt[C]:
        answer[a + b + c] = 'C'
        # 전전 날과 전 날 B가 아닌 다른 것 선택
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c + 1, [prev[1], C]):
                return True
    return False

dfs(0, 0, 0, [0, 0])
print(-1)