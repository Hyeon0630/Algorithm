hi, mi = input().split()
hi = int(hi)
mi = int(mi)

ho = hi
mo = mi - 45

if mo < 0 : 
    ho -= 1
    mo += 60

if ho < 0 : 
    ho += 24

print(ho, mo)