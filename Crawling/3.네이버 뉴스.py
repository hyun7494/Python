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
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20230117&page=%d' %pg

    html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    #print(html)

    # 문서객체 생성
    dom = bs(html, 'html.parser')
    
    # 현재 페이지 번호
    currentPage = dom.select_one('#main_content > div.paging > strong').text

    if pg > int(currentPage):
        break

    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        link = tag_a['href']

        # print('count :', count)
        # print('title :', title.strip())
        # print('link :', link.strip())

        sheet.append([count, title.strip(), link.strip()])
        print('%d건 저장...' % count)
    
        count += 1

    pg += 1

# 엑셀파일 저장
workbook.save('C:/Users/java1/Desktop/News.xlsx')
workbook.close()

print('프로그램 종료')