import sys
input = sys.stdin.readline

# 0 ~ 999999
# 100과의 비교 -> abs(want - 100)
# want와 가장 가까운 수 만들기 -> min
# abs((want - 가까운 수) + 가까운 수 길이)
want = int(input())
broken = int(input())
b = []
if broken != 0:
    b = list(input().split())

answer = abs(want - 100)

for i in range(1000000):
    temp = str(i)
    sp = 0

    while sp < len(temp):
        if temp[sp] not in b:
            sp += 1
        else:
            break

    if sp == len(temp):
        answer = min(answer, abs(i - want) + len(str(i)))

print(answer)