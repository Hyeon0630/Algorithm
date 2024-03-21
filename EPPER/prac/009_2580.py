import sys
input = sys.stdin.readline

dict = {}
s = []
for i in range(9):
    s.append(list(map(int, input().split())))

def solution(s):
    c = [0]*27
    # 0~8까지 돌며 0인 개수 카운트
    for i in range(0, 9):
        rcnt = 0
        ccnt = 0
        for j in range(0, 9):
            if s[i][j] == 0:
                rcnt += 1
                if i//3 == 0 and j//3 == 0:
                      c[18] += 1
                elif i//3 == 0 and j//3 == 1:
                      c[19] += 1
                elif i//3 == 0 and j//3 == 2:
                      c[20] += 1
                elif i//3 == 1 and j//3 == 0:
                      c[21] += 1
                elif i//3 == 1 and j//3 == 1:
                      c[22] += 1
                elif i//3 == 1 and j//3 == 2:
                      c[23] += 1
                elif i//3 == 2 and j//3 == 0:
                      c[24] += 1
                elif i//3 == 2 and j//3 == 1:
                      c[25] += 1
                elif i//3 == 2 and j//3 == 2:
                      c[26] += 1
            if s[j][i] == 0:
                ccnt += 1
        c[i] = rcnt
        c[i+9] = ccnt

    while(1 in c):
        for i in range(27):
            if c[i] == 1:
                
    # dict에 1(행), 2(열), 3(박스)
    # 몇번 행, 열, 박스인지
    # 카운트된 개수

    # while 카운트 된 개수 배열에 0이 있을 때까지
    # dict 안에서 카운트된 개수가 1인 애들 선택
    # temp 배열에 해당 행, 열, 박스 받아옴 받아올 때 0이되는 행, 열 정보도 a, b에 저장
    # 45에서 sum(temp) 빼서 0인 애 값 변경
    # a, b가 있는 위치 dict 카운트 수도 변경

    
    return s

p = solution(s)

for i in range(9):
        for j in range(9):
            print(p[i][j], end = " ")
        print()