import sys
input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for i in range(N))


# 생각을 하자
# w[0]에서 w[1], w[2], w[3]을 돌아야 함
# 한 트리 끝까지 갈 동안 가중치 합 저장할 cnt가 있고
# cnt <= ans이면 ans = cnt
# 재귀를 돌아야 할 듯
# 아래 가중치들의 합이 필요할 거고
# 함수는 그럼 밑 노드들에서 가장 작은 가중치 합
# 인자로는 윗 노드들 번호(부모 노드 인덱스 int, 자식 노드 인덱스 list, ans)


def Solution(w):
    ans = 0
    cnt = []
    for i in w:
        for j in w[i]:
            if j != 0:
                cnt.append(i)

    return ans

print(Solution(W))