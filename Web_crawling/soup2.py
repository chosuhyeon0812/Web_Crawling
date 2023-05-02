import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import requests

context = ssl._create_unverified_context()

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%A7%84%EC%A3%BC%EB%82%A0%EC%94%A8%27')
soup = BeautifulSoup(webpage, 'html.parser')
#print(soup)

#dust = soup.find('div', 'item_today level2')
#print(dust)

#temps = soup.find('div', 'temperature_text')
#print(temps)
#print("진주 : "+temps.text.strip())

# summary = soup.find('p', 'summary')
# print(summary)
# print(summary.text.strip())

dl_summary = soup.find('dl', 'summary_list')
print(dl_summary)
print(dl_summary.text.strip())
