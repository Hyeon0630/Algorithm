count = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))

    global count # 참조
    count += 1

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧센 횟수는 {}번 입니다.".format(count))