from DataAuth import Authentication
from datetime import date, datetime # 현재 시각 반환 라이브러리
import urllib.request
import DataAuth
import DataRefine

date = str(datetime.now())
date = date[:date.rfind(' ')]
resultData = 'default'

def GetPeriod():
    startDate = "2016-01-01" # 네이버 API 검색 가능일
    endDate = date # 금일
    timeUnit = "week" # 고정

    return startDate, endDate, timeUnit

def GetKeyword(startDate, endDate, timeUnit):

    keyWord1 = '["클라우드"]'
    keyWord2 = '["클라우드 보안"]'

    body = '''{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"keywordGroups\":[
                {\"groupName\":\"그룹 1\",\"keywords\":%s}, 
                {\"groupName\":\"그룹 2\",\"keywords\":%s}
                ]}''' % (startDate, endDate, timeUnit, keyWord1, keyWord2)

    return body

url = "https://openapi.naver.com/v1/datalab/search"

startDate, endDate, timeUnit = GetPeriod()
body = GetKeyword(startDate, endDate, timeUnit)

request = urllib.request.Request(url)
request = Authentication(request)
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
resCode = response.getcode()

if(resCode==200):
    response_body = response.read()
    resultData = (response_body.decode('utf-8'))
else:
    print("Error Code:" + resCode)

def GetCrawlingResult():
    return resultData
