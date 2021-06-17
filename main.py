#노마드 코더 강의 보면서 웹 크롤링 해보기 / 응용?
#requests, beautifulsoup4를 import 하기 위해 cmd로 설치했음
import requests
from bs4 import BeautifulSoup
result = requests.get("https://cafe.naver.com/ArticleList.nhn?search.clubid=27877258&search.menuid=109&search.boardtype=L")
soup = BeautifulSoup(result.text, "html.parser") #html text를 정리하는 느낌인듯


pagination = soup.find_all("div",class_='prev-next')
# page = pagination.find_all("a")
print(pagination)
spans = []
for page in pagination:
   spans.append(page.find_all("a"))
   print(spans)