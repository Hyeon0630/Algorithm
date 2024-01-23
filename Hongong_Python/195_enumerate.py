example_list = ["요소A", "요소B", "요소C"]

print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".findformat(i, value))