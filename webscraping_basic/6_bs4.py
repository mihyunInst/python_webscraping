import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) : soup객체에서 처음 발견되는 a 엘리먼트 출력
# print(soup.a.attrs) : a 엘리먼트  속성 정보를 출력
# print(soup.a["href"]) : a 엘리먼트  속성값 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"}))
print(soup.find("li",attrs={"class":"rank01"}).a) # li 태그에서 해당 클래스 찾은 후 a 태그 찾기