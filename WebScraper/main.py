from page import find_page, extract_notice 
#최대 page를 계산하는 함수, request생성

last_page = find_page()

notice = extract_notice(last_page)
print(notice)