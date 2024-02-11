arr = input().split('-')

result = 0

t = arr[0].split('+')
for i in range(len(t)):
    result += int(t[i])

for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)