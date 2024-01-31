from urllib import request

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("./img/363_output.png", "wb")
file.write(output)
file.close()