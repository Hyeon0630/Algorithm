number = input("정수를 입력하세요 > ")
last_number = number[-1]

if last_number in "02468":
    print("짝수입니다.")

if last_number in "13579":
    print("홀수입니다.")