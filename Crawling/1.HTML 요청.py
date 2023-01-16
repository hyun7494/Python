"""
날짜 : 2023/01/16
이름 : 김현준
내용 : 파이썬 HTML 요청 실습하기
pip install requests
"""

import requests as req

url = 'https://www.naver.com'

html = req.get(url).text
print(html)