    # dic key값 나올 때까지 전진
    # 방향, 움직인 시간, 시작 좌표를 함수에 전달, 최종 좌표 받기
    # 사과(1)을 만나면 지금 칸에 3을 넣고 한 칸 앞으로
    # 길이 저장할 length = 0에 추가하고 length != 0이면 마지막 좌표는 항상 0으로 되돌리자
    # 이때부터는 3도 하나씩 전진 (하나는 다시 0으로, 하나는 3으로)
    # 만약 전진해서 2 또는 3을 만나면 초를 출력하고 끝
    # dic key값나오면 'L' / 'D' 확인해서 진행 방향 변경
    # 방향 변경은 어떻게 반영할까
    # 일단 u, d, l, r를 두어서 방향 결정
    # 함수를 만들어 direction, x, y / 반환도

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
pan = [[0 for i in range(N+2)] for j in range(N+2)]

for i in range(N+2):
    pan[0][i] = 2
    pan[N+1][i] = 2
    pan[i][0] = 2
    pan[i][N+1] = 2

for i in range(K):
    a, b = map(int, input().split())
    pan[a][b] = 1 # 1은 사과

L = int(input())
drc = {}

for i in range(L):
    X, C = input().split()
    X = int(X)
    C = str(C)
    drc[X] = C

rst = 0

def go(direction, x, y):
    px, py = x, y
    if direction == 0: # r
        y += 1
    elif direction == 1: # d
        x += 1
    elif direction == 2: # l
        y -= 1
    elif direction == 3: # u
        x -= 1
    return x, y, px, py

def solution(p):
    x = 1
    y = 1
    s = 1
    cnt = 0
    result = 0
    length = 1
    direction = 0
    m = []
    n = []
    k = 0
    for i in drc.keys():
        for j in range(s, i+1):
            """ if length >= 2:
                p[px][py] = 0
                x, y, px, py = go(direction, x, y)
                p[px][py] = 3
            else:
                x, y, px, py = go(direction, x, y)
                p[px][py] = 0
            if p[x][y] == 2 or p[x][y] == 3:
                result = 1
                return j
            elif p[x][y] == 1: #사과
                p[x][y] = 0
                p[px][py] = 3
                length += 1 """


            x, y, px, py = go(direction, x, y)
            if p[x][y] == 2 or p[x][y] == 3:
                result = 1
                return j
            elif p[x][y] == 1: #사과
                p[x][y] = 0
                p[px][py] = 3
                m.append(px)
                n.append(py)
                length += 1
            elif p[x][y] == 0 and length > 1:
                p[px][py] = 3
                p[m[k]][n[k]] = 0
                m.append(px)
                n.append(py)
                k += 1

            
        c = drc[i]
        if c == 'D':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction + 3) % 4
        s = i + 1

    if result == 0:
        while p[x][y] != 2 and p[x][y] != 3:
            x, y, px, py = go(direction, x, y)
            cnt += 1
        return X + cnt

rst = solution(pan)
print(rst)