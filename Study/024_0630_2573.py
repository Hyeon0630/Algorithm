import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for i in range(n)]

# 빙산이 몇 덩이인지 구분하는 프로그램
# 이 프로그램이 3이란 값이 될 때까지 반복
# 프로그램이 반복되는 동안 주변 값에 따라서 빙산의 높이 감소

