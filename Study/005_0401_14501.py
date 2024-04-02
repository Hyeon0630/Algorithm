import sys
input = sys.stdin.readline

N = int(input()) # 일하는 날
info = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for i in range(N+1)] # 인덱스일부터 퇴사일까지 받을 수 있는 최대 보수 따라서 출력은 dp[0]

for i in range(N-1, -1, -1): # 뒤에서부터
    if info[i][0] + i > N: # 퇴사일을 넘어갈 수 있으니
        dp[i] = dp[i+1] # 퇴사일을 넘어갈 경우에는 그대로
    else:
        dp[i] = max(dp[i+1], dp[i+info[i][0]]+info[i][1]) 
        # 오늘부터 퇴사 전까지의 보수 최댓값은
        # 오늘 일하지 않았을 때 VS 일해서 info[i][0] 뒤의 dp에 저장된 값과 이 날의 보수를 합한 값
    
print(dp[0])