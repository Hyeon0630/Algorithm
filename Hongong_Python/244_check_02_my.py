# 10 * 10 => 1
# 10을 분할
# (8,2), (7,3), (6,4), (6,2,2), (5,5), (5,3,2), (4,4,2), (4,3,3), (4,2,2,2), (3,3,2,2), (2,2,2,2,2)
# 11가지 + 1가지 = 12가지
# 12H10 = 21C10
# nCr = n!/r!(n-r)!

MIN = 2

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
def ncr(n, r):
    a = factorial(n)
    b = factorial(r)*factorial(n-r)
    result = int(a/b)
    return result

def count_n(n):
    count = 1
    for i in range(2, n//2 + 1): # 10 - 2, 3, 4, 5 // 9 - 2, 3, 4
        case = [n-i, i]
        count += 1
        for j in case:
            if j != 2:
                count += 1
                count_n(j)
    return count

# 10 * 10 이므로
n = count_n(10)
r = 10
result = int(ncr(n+r-1, r))
print(result)