numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:
    check = i % 2
    l = len(str(i))

    if check == 1 :
        print(i, "는 홀수입니다.")
    else:
        print(i, "는 짝수입니디.")

    print(i, "는", l, "자릿수입니다.")
    print()
