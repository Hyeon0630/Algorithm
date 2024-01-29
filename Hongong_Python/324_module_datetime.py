import datetime as d

print("# 현재 시각 출력하기")
now = d.datetime.now()
print(now.year, "년", sep="")
print(now.month, "월", sep="")
print(now.day, "일", sep="")
print(now.hour, "시", sep="")
print(now.minute, "분", sep="")
print(now.second, "초", sep="")
print()

print("# 시간을 포멧에 맞추어 출력하기")
output_a = now.strftime("%Y.%m.%d %H.%M.%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
                                            now.month,\
                                            now.day,\
                                            now.hour,\
                                            now.minute,\
                                            now.second
                                            )
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))
print(output_a)
print(output_b)
print(output_c)
print()