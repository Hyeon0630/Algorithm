q = str(input())
arr = list(q)
if '-' in arr:
    if arr.count('-') == 2: # --
        a, b, c = map(int, q.split('-'))
        print(a - b - c)
    elif '+' not in arr: # -
        a, b = map(int, q.split('-'))
        print(a - b)
    elif arr.index('+') < arr.index('-'):
        q = q.replace('+', '-')
        a, b, c = map(int, q.split('-'))
        print(a + b - c)
    else:
        q = q.replace('+', '-')
        a, b, c = map(int, q.split('-'))
        print(a - (b + c))
else:
    temp = list(map(int, q.split('+')))
    print(sum(temp))