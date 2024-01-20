""" import datetime

time = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    str(time.year), 
    str(time.month),
    str(time.day),
    str(time.hour),
    str(time.minute),
    str(time.second)
)) """

import datetime

time = datetime.datetime.now()

print("{0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(
    time.year,
    time.month,
    time.day,
    time.hour,
    time.minute,
    time.second
))