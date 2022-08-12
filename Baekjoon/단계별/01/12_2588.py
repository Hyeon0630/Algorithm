n = int(input())
s = int(input())

r = n*s
a = s//100
s -= 100*a 
b = s//10
s -= 10*b 
c = s

print(n*c)
print(n*b)
print(n*a)
print(r)