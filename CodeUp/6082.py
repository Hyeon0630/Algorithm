n = int(input())

for i in range(1, n+1) :
    if (i/10)!=0 :
        a = (i/10)%3
    else : 
        a = 3
    if (i%10)!=0 :
        b = (i%10)%3
    else : 
        b = 3
    if (a == 0) & (b == 0) :
        print("XX", end = ' ')
    elif (a == 0) & (b != 0) : 
        print("X", end = ' ')
    elif (a != 0) & (b == 0) : 
        print("X", end = ' ')
    else :
        print(i, end = ' ')