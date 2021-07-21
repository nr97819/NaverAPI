from typing import Text
from DataAuth import Authentication
from datetime import date, datetime # 현재 시각 반환 라이브러리
import urllib.request

date = str(datetime.now())
date = date[:date.rfind(' ')]

url = "https://openapi.naver.com/v1/datalab/search"

keyWord = []

def SetKeyWord(text):
    split1, split2 = text
    temp = '[\"%s\", \"%s\"]' % (split1, split2)
    global keyWord
    keyWord = temp
    # return text

def GetPeriod():
    startDate = "2016-01-01" # 네이버 API 검색 가능일
    endDate = date # 금일
    timeUnit = "week" # 고정

    return startDate, endDate, timeUnit

def GetFormat(startDate, endDate, timeUnit, keyWord):
    body = '''{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"keywordGroups\":[
                {\"groupName\":\"그룹1\",\"keywords\":%s}]}''' % (startDate, endDate, timeUnit, keyWord)
    return body

def GetHttpResponse(keyWord):
    startDate, endDate, timeUnit = GetPeriod()
    body = GetFormat(startDate, endDate, timeUnit, keyWord)

    request = urllib.request.Request(url)
    request = Authentication(request)
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    resCode = response.getcode()

    if(resCode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + resCode) # 예외 처리
        return None

'GetCrawlingResult()의 #만 지우면 목표결과 완성!'
def GetCrawlingResult():
    return GetHttpResponse(keyWord)#, GetHttpResponse(keyWord2) # 각각의 JSON 파일

# inputValue = input('첫번째 키워드 2개를 입력해주세요!\n예시) 오징어,땅콩\n')
# keyWord1 = SetKeyWord(inputValue)