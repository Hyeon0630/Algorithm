import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("오전 {0}시 입니다.".format(now.hour))
elif now.hour >= 12:
    print("오후 {0}시 입니다.".format(now.hour))