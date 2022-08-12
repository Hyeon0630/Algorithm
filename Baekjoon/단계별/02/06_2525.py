hi, mi = input().split()
n = int(input())
hi = int(hi)
mi = int(mi)
ho = hi + n//60
mo = mi + n%60

if mo >= 60 : 
    ho += 1
    mo -= 60

if ho >= 24 : 
    ho -= 24

print(ho, mo)