# 사람 수 N 입력값 저장
N = int(input())

# N+1개의 리스트 P 생성
P = list(map(int, input().split()))
#P = [0] * int(N+1)

# P에 입력값 저장, 배열 만들 때 index 1~N
#for i in range(1, N):
#    P[i] = input().split()

# 마지막 사람이 가장 오래 걸리도록 - 오름차순
# 삽입 정렬
for j in range(2, N):
    for k in range(1, j-1):
        if P[j] <= P[k]:
            tmp = P[j]
            for l in range[j-1:k]:
                P[l+1] = P[l]
            P[k] = tmp

# 대기 시간 총 합에서 Pi는 N-i+1번
sum = int(0)
for m in range(1, N):
    sum += int(P[m] * (N-m+1))

print(sum)