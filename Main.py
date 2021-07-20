import DataRefine

def Main():
    url = "https://openapi.naver.com/v1/datalab/search"

    # 출력할 연도 입력 받기
    startDate, endDate, timeUnit = GetPeriod()
    # 출력할 keyWord 입력 받기
    body = GetKeyword(startDate, endDate, timeUnit)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",clientId)
    request.add_header("X-Naver-Client-Secret",clientSecret)
    request.add_header("Content-Type","application/json")

    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    resCode = response.getcode()

    if(resCode==200):
        response_body = response.read()
        resultData = (response_body.decode('utf-8'))
    else:
        print("Error Code:" + resCode)

    refinedData = DataRefine.DataRefining(resultData)

    PrintInfo(refinedData)

if __name__ == '__main__':
    Main()