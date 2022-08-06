n = int(input())
a = input().split()
min = 0

for i in range(n) : 
    a[i] = int(a[i])

min = a[0]

for i in range(n-1) : 
   if min >= a[i+1] :
    min = a[i+1]

print(min)