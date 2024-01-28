list = ["100", "200", "300", "400", "하이"]
result = []

for i in list:
    try:
        float(i)
        result.append(i)
    except:
        pass

print("{}내부에 있는 숫자는".format(list))
print("{}입니다.".format(result))