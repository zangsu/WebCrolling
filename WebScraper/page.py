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
    sURL = URL[:-6]
    notice = []

    # for page in range(last_page):
    #     result = requests.get(f"{sURL}&page={page+1}")
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    #table = soup.find_all("tr")
    table = soup.find_all("a",class_="article")
    for element in table:
        #head = element.find("a",class_="article")
        head = [element.text]

        head[0] = head[0].replace("\n", "")
        head[0] = head[0].replace("\t", "")

        top1 = 0
        tail = len(head[0])
        i = 0
        while(head[0][i] == ' '):
            top1 = top1+1
            i+=1
        while(head[0][i] != ' '):
            i+=1
        i = len(head[0])
        while(head[0][i-1] == " "):
            tail = tail-1
            i-=1
        head[0] = head[0][top1:tail]

        notice.append(head)

        # name = element.find("a", class_="m-tcol-c")
    print(notice)
        #notice.append()
    return notice