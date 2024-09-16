import sys
input = sys.stdin.readline
# https://fre2-dom.tistory.com/54

N, M = map(int, input().split()) # N = 7, M = 2
book = list(map(int, input().split()))
# 책 위치가 양수인 것과 음수인 것을 나누어

p = [] # 책 위치 양수
m = [] # 책 위치 음수

for i in book:
    if i > 0:
        p.append(i)
    else:
        m.append(-i)

p.sort() # p = [2, 11]
m.sort() # m = [6, 28, 29, 37, 39]

# 최댓값 계산 - 마지막에 갈 곳(*2 하지 않음)
pm = p.pop()
mm = m.pop()
last = max(pm, mm)
p.append(pm)
m.append(mm)

result = 0

# 양수 책
# len(p) // M = 1
# len(m) // M = 2
for i in range(0, len(p)//M + 1):
    p_p = M * i
    result += p[p_p] * 2

# 음수 책
for i in range(0, len(m)//M + 1):
    result += m[i] * 2

# 가장 멀리 있는 책은 돌아오지 않으므로 한 번 이동 거리를 빼준다
result -= last

print(result)