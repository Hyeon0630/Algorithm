from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨 읽기 기상청 RSS
    target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeaBeautifulSoup을 사용해 웹 페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    output = ""
    # location 태그 찾기
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}</br><hr>".format(location.select_one("tmn").string, location.select_one("tmx").string)

    return output