import random as r
print("# ramdom 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 리턴
print("- random():", r.random())
print()

# uniform(min, max): 지정한 범위 사이의 float를 리턴
print("- uniform(10, 20):", r.uniform(10, 20))
print()

# randrange(): 지정한 범위 사이의 int를 리턴
# randrange(max): 0부터 max 사이의 int를 리턴
# randrange(min, max): min부터 max 사이의 int를 리턴
print("- randrange(10):", r.randrange(10))
print("- randrange(10, 20):", r.randrange(10, 20))
print()

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print("- choice([1, 2, 3, 4, 5]):", r.choice([1, 2, 3, 4, 5]))
print()

# shuffle(list): 리스트 내부에 있는 요소를 랜덤하게 섞기
print("- shuffle([1, 2, 3, 4, 5]):", r.shuffle([1, 2, 3, 4, 5]))
print()

# sample(list, k = <숫자>): 리스트 내부에 있는 요소 중에 k개를 선택
print("- sample([1, 2, 3, 4, 5], k = 2):", list(r.sample([1, 2, 3, 4, 5], k = 2)))
print()