""" input = int(input("정수를 입력하시오"))

if input > 0:
    print("양수입니다.")
if input < 0:
    print("음수입니다.")
if input == 0:
    print("0입니다.") """

input = int(input("정수를 입력하시오"))

if input > 0:
    print("양수입니다.")
elif input < 0:
    print("음수입니다.")
else:
    print("0입니다.")