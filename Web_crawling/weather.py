import requests
from bs4 import BeautifulSoup

# 파싱할 웹 페이지의 URL 주소
url = 'https://www.naver.com'

# Requests 모듈을 사용하여 해당 URL 주소의 HTML 문서를 가져옴
response = requests.get(url)

# HTML 문서를 BeautifulSoup 객체의 인자로 전달하여 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 이후 soup 객체를 이용하여 원하는 정보를 추출


#검색할 지역 입력받기
location = input("지역을 입력하세요: ")

# 네이버에서 날씨 정보 가져오기
url = f"https://search.naver.com/search.naver?query"

res = requests.get(url)
res.raise_for_status()

#beautifulSoup 겍체 생성
soup = BeautifulSoup(res. text, "html.parser")

# 현재 온도 가져오기
curr_temp = soup.find("span", attrs={"class": "todaytemp"}).text


# 오늘의 날씨 요약 가져오기
weather_summary = soup.find("p", attrs={"class":"cast_txt"}).text
 
 #오늘의 최고/최저 온도 가져오기
temp_info = soup.find("span", attrs={"class": "min"}).text + " / " + soup.find("span", attrs={"class": "max"}).text

# 결과 출력
print(f"현재 {location}의 기온은 {curr_temp}℃입니다.")
print(f"{weather_summary}")
print(f"최저 / 최고 기온 : {temp_info}")