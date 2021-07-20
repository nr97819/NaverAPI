import DataAuth
import DataCrawl
import DataRefine
import DataVisual
import urllib.request

def Main():

    url = "https://openapi.naver.com/v1/datalab/search" # Crawl Part

    # 출력할 연도 입력 받기
    startDate, endDate, timeUnit = DataCrawl.GetPeriod() # Static Value ...
    
    # 출력할 keyWord 입력 받기 <-----------------
    body = DataCrawl.GetKeyword(startDate, endDate, timeUnit)  # Static Value ...

    request = urllib.request.Request(url)
    DataAuth.Authentication(request)
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    resCode = response.getcode()

    if(resCode==200):
        response_body = response.read()
        resultData = (response_body.decode('utf-8'))
    else:
        print("Error Code:" + resCode)
    
    refinedData = DataRefine.DataRefining(DataCrwal.resultData)

    DataVisual.PrintInfo(refinedData)

if __name__ == '__main__':
    Main()