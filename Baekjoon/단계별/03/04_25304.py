X = int(input())
N = int(input())
p = 0
for i in range(N) : 
    a, b = input().split()
    a = int(a)
    b = int(b)
    p += a*b

if p == X : 
    print("Yes")
else : 
    print("No")