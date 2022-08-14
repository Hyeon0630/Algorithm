N = int(input())
a = list(map(int, input().split()))
max = max(a)
for i in range(N) : 
    a[i] = a[i]/max*100

print(sum(a)/N)