"""
날짜 : 2023/01/16
이름 : 김현준
내용 : 파이썬 네이버 뉴스 크롤링 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

# 엑셀 파일 생성
workbook = Workbook()
sheet = workbook.active


pg = 1
count = 1

while True:
    # HTML 요청
    url = 'https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=%d' %pg

    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    #print(html)

    # 문서객체 생성
    dom = bs(html, 'html.parser')
    
    # 현재 페이지 번호         
    currentPage = dom.select_one('#main_content > div.paging > strong').text

    contTitle = bs.find('dd')

    if pg > 100000:
        break

    for li in range(100000):
        contTitle = bs.find('dd').text
        symptom = bs.find().text
        link = tag_a['href']

        # print('count :', count)
        # print('title :', title.strip())
        # print('link :', link.strip())

        sheet.append([count, contTitle.strip(), link.strip()])
        print('%d건 저장...' % count)
    
        count += 1

    pg += 1

# 엑셀파일 저장
workbook.save('C:/Users/java1/Desktop/News.xlsx')
workbook.close()

print('프로그램 종료')