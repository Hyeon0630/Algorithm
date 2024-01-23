limit = 10000

i = 1
result = 0

while result < limit:
    result += i
    if result > limit: 
        break
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, result))