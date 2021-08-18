from typing import Text
from DataAuth import Authentication
from datetime import date, datetime # 현재 시각 반환 라이브러리
import urllib.request

date = str(datetime.now())
date = date[:date.rfind(' ')]

URL = "https://openapi.naver.com/v1/datalab/search"
keyWord = []

# Summary:
# 입력 키워드 2개 분리
# param:
# 입력 문자열
# returns:
# 없음(전역변수에 저장)
def SetKeyWord(text):
    split1, split2 = text
    temp = '[\"%s\", \"%s\"]' % (split1, split2)
    global keyWord
    keyWord = temp
    # return text

# Summary:
# Naver API 사용한, 검색 시작일/종료일/간격 정보 반환
# param:
# 없음
# returns:
# 검색 시작일/종료일/간격 정보 반환
def GetPeriod():
    startDate = "2016-01-01" # 네이버 API 검색 가능 시작일
    endDate = date
    timeUnit = "week" # 고정

    return startDate, endDate, timeUnit

# Summary:
# 검색 요청사항을 JSON 형식으로 정제 (Naver API가 요구)
# param:
# 검색 시작일/종료일/간격/검색 키워드
# returns:
# JSON
def GetFormat(startDate, endDate, timeUnit, keyWord):
    body = '''{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"keywordGroups\":[
                {\"groupName\":\"그룹1\",\"keywords\":%s}]}''' % (startDate, endDate, timeUnit, keyWord)
    return body

# Summary:
# Naver API 요청 결과 반환
# param:
# 검색 키워드
# returns:
# http 요청 결과
def GetHttpResponse(keyWord):
    startDate, endDate, timeUnit = GetPeriod()
    body = GetFormat(startDate, endDate, timeUnit, keyWord)

    request = urllib.request.Request(URL)
    request = Authentication(request)
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    resCode = response.getcode()

    if(resCode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + resCode) # 예외 처리
        return None

# Summary:
# main에서 크롤링 이용 수단
# param:
# 없음
# returns:
# GetHttpResponse() 함수 return 값 전달
def GetCrawlingResult():
    return GetHttpResponse(keyWord)