"""
날짜 : 2023/01/11
이름 : 김현준
내용 : 파이썬 상속 실습하기
"""

from sub2.StockAccount import StockAccout

kb = StockAccout('kb증권', '101-12-1110', '홍길동', 50000, '삼성전자', 10, 60000)
kb.deposit(100000)
kb.sell()