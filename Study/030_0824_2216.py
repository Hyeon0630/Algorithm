import sys
input = sys.stdin.readline

# a, f / b, d / c, e
# 0, 5 / 1, 3 / 2, 4
o = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

result = 0

for i in range(6):
    sum = 0
    top = D[0][i]
    bottom = D[0][o[i]]

    for j in range(N):
        ti = D[j].index(top)
        new = D[j][o[ti]]
        temp = []
        temp.append(top)
        temp.append(new)

        if 6 in temp:
            if 5 in temp:
                sum += 4
            else:
                sum += 5
        else:
            sum += 6

        if j < N - 1:
            top = new
    
    result = max(result, sum)

print(result)