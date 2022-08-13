m = int(input())
t = m//10
o = m%10
count = 0
while True : 
    n = (t+o)%10+o*10
    t = n//10
    o = n%10
    count += 1
    if m == n :
        break
print(count)