#노마드 코더 강의 보면서 웹 크롤링 해보기 / 응용?
#requests, beautifulsoup4를 import 하기 위해 cmd로 설치했음
import requests
from bs4 import BeautifulSoup
URL = "https://cafe.naver.com/ArticleList.nhn?search.clubid=27877258&search.menuid=109&search.boardtype=L&search.totalCount=134&search.page=1"
#URL은 나중에 적당한 걸로 바꾸기(현재 네이버 카페는 로그인 안하면 들어가기 힘든듯함)
def find_page():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser") #html text를 정리하는 느낌인듯


    pagination = soup.find_all("div",class_='prev-next')
    #pages = pagination.find_all("a")
    # -> pagination이 한가지 요소로 구성된 리스트라서 그런지 요소를 찾을 수 없다고 뜸
    spans = []
    for page in pagination:
        spans.append(page.find_all('a'))
    #    #find_all("a").string을 사용하니 string이란 속성이 없다고 그럼
    #    #find("a").string을 사용하니 하나만 추출됨
    #    #print(spans)
    pages = spans[0]
    spans = []
    for i in pages: 
     spans.append(int(i.string))
    #  page 수 추출
    max_page = spans[-1]

    return max_page

def extract_notice(last_page):
    notice = []
    for page in range(last_page):
        result = requests.get(f"{URL}&page={page+1}")
        print(result)

    return notice