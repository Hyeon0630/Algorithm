# yes!!, 100, 3

list = [52, 273, 32, 72, 100]

try:
    input = int(input("정수 입력 > "))
    print("{}번째 요소: {}".format(input, list[input - 1]))
except ValueError as exception:
    print("정수를 입력하세요.")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요.")
    print("exception:", exception)