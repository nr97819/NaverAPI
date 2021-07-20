# 기본
from sys import stdout

# Naver API
import urllib.request
import json

# matplotlib
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

# Naver API
clientId = "gKjj14gCwEygk42XREsy"
clientSecret = "EDB3_6DXf2"

# 한글 폰트 (맑은 고딕 경로)
fromLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fromLocation).get_name()
matplotlib.rc('font', family=fontName)

'--------------- 실질직 코드 ---------------'

def GetPeriod():
    # print('시작 입력(YYMMDD) :')
    print('검색할 년도 입력 :(YY)')
    inputText = input()
    # startDate = "20%s-%s-%s" % (inputText[0:2], inputText[2:4], inputText[4:])
    startDate = "20%s-01-01" % inputText
    # startDate = "20%s-%s-%s" % (inputText[0], inputText[1], inputText[2])
    # YY-MM-DD

    # print('종료일 입력(YYMMDD) :')
    # inputText = input()
    # endDate = "20%s-12-31" % (inputText[0:2], inputText[2:4], inputText[4:])
    endDate = "20%s-12-31" % inputText

    timeUnit = "month" # 고정

    return startDate, endDate, timeUnit

def GetKeyword(startDate, endDate, timeUnit):
    print('[조회할 키워드 2개를 입력해주세요.]')
    print('1번째 키워드 입력 :')
    keyWord = "[\"%s\"," % input()

    print('2번째 키워드 입력 :')
    keyWord += "\"%s\"]" % input()

    body = '''{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"keywordGroups\"
:[{\"groupName\":\"검색 그룹 1\",\"keywords\":%s}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}''' % (startDate, endDate, timeUnit, keyWord)

    return body

def PrintInfo(addrData):
    list = []

    for i in range(12):
        temp = addrData['results'][0]['data'][int(i)]['ratio']
        list.append(round(temp, 2))

    'ro' 'b' 'bs' 'g' # 빨간점, 파랑, 파란네모, 초록
    plt.plot(    [1,2,3,4,5,6,7,8,9,10,11,12], 
                [list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11]],
                0.9, 
                color='green')
    plt.xlabel('월별')
    plt.ylabel('검색률')
#      plt.bar(
# [1,2,3,4,5,6,7,8,9,10,11,12], 
# [list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11]], 'b') # x도 1부터 시작

    # 표시 범위
    plt.axis([1, 12, 0, 100]) # x축의 범위 0~10 / y축의 범위 0~20

    plt.show()

    print('''
    -----------------------------------------
    - 정상적으로 통계 파일이 추출되었습니다 -
    -----------------------------------------
    ''')

def DataRefining(resultData):
    refinedData = json.loads(resultData)
    # 경로는 본인 PC에 맞게 설정
    writePath = r'C:/NaverAPI/NaverAPI/search_naver_data.json'
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False, # 오히려 섞임
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData

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

    refinedData = DataRefining(resultData)

    PrintInfo(refinedData)

if __name__ == '__main__':
    Main()