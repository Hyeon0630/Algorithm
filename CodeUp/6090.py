a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

# a am+d
s = a
while n != 1 :
    s = s*m+d
    n -= 1

print(s)