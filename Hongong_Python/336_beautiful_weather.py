from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨 읽기 기상청 RSS
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeaBeautifulSoup을 사용해 웹 페이지 분석
# target을 html.parser로 읽기
soup = BeautifulSoup(target, "html.parser")

# location 태그 찾기
# soup.select() - 특정 이름을 가진 태그를 모두 찾아줌
# soup.select_one() - 특정 이름을 가진 태그를 하나만 찾아줌
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()