import requests
from bs4 import BeautifulSoup

# 네이버 날씨 페이지의 URL 주소
url = "https://weather.naver.com/today/02173670"

# Requests 모듈을 사용하여 해당 URL 주소의 HTML 문서를 가져옴
response = requests.get(url)

# HTML 문서를 BeautifulSoup 객체의 인자로 전달하여 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 현재 온도를 추출하여 출력
curr_temp = soup.find("span", attrs={"class": "todaytemp"})
if curr_temp:
    print("현재 온도: " + curr_temp.text + "℃")
else:
    print("현재 온도 정보를 찾을 수 없습니다.")

