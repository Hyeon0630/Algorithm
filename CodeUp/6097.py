h, w = input().split()
h = int(h)
w = int(w)
array = []
for i in range(h) : 
    array.append([])
    for j in  range(w) : 
        array[i].append(0)

n = int(input())
for i in range(n) :
    l, d, x, y = input().split()
    if int(d) == 1 : 
        for j in range(int(l)) : 
            array[int(x)+j-1][int(y)-1] = 1
    else : 
        for j in range(int(l)) : 
            array[int(x)-1][int(y)+j-1] = 1

for i in range(h) : 
    for j in range(w) : 
        print(array[i][j], end = ' ')
    print()

# input =[]
# for i in range(n) :
#     input.append([]) 
#     for j in range(4) :
#         input[i].append(input().split())
#         # 0 길이 1 방향 2 x 3 y

# for i in range(n) :
#     for j in range(4) :
#         input[i][j] = int(input[i][j])

# for i in range(n) :
#     if input[i][1] == 0 : 
#         for j in range(input[i][3]-1, input[i][3]-1+input[i][0], 1) : 
#             array[input[i][2]-1][j] = 1
#     elif input[i][1] == 1 :
#         for j in range(input[i][2]-1, input[i][2]-1+input[i][0], 1) : 
#             array[j][input[i][3]-1] = 1        