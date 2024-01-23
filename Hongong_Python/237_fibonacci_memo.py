memo = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = result
        return result
    
for i in range(10, 51, 10):
    print("fibonacci({}):".format(i), fibonacci(i))