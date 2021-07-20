from DataAuth import Authentication
from datetime import date, datetime # 현재 시각 반환 라이브러리
import urllib.request
import DataAuth
import DataRefine

date = str(datetime.now())
date = date[:date.rfind(' ')]

# 기간 수정 예정
def GetPeriod():
    startDate = "2016-01-01"
    endDate = date # 금일
    timeUnit = "week" # 고정

    return startDate, endDate, timeUnit

def GetKeyword(startDate, endDate, timeUnit):
    keyWord = "[\"%s\"," % startDate
    keyWord += "\"%s\"]" % endDate

    body = '''{\"startDate\":\"%s\",
               \"endDate\":\"%s\",
               \"timeUnit\":\"%s\",
               \"keywordGroups\"
               :[{\"groupName\"
               :\"검색 그룹 1\",
                \"keywords\":%s}],
                \"device\":\"pc\",
                \"ages\":[\"1\",\"2\"],
                \"gender\":\"f\"}''' % (startDate, endDate, timeUnit, keyWord)

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

temp = resultData
