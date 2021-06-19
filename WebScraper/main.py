from page import find_page, extract_notice 
#최대 page를 계산하는 함수, request생성

max_page = find_page()

last_page = extract_notice(max_page)