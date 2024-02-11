N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

price.pop()

result = price[0] * length[0]
min = price[0]

for i in range(1, len(price)):
    if price[i] <= min:
        min = price[i]
    result += length[i] * min

print(result)