from page import find_page, extract_notice 
from save import save_to_file
#최대 page를 계산하는 함수, request생성

last_page = find_page()

notice = extract_notice(last_page)
print(notice)
#for element in notice:
#    print(f"제목 : {element[0]}, 작성자 : {element[1]}, 작성일 : {element[2]}")  
    
#save_to_file(notice)