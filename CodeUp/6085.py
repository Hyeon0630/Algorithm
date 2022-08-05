w, h, b = input().split()
w = int(w) 
h = int(h)
b = int(b)
n = float(w*h*b/8/1024/1024)

print(format(n, ".2f"), "MB")