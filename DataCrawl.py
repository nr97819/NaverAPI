# 기본
from sys import stdout

# Naver API
import urllib.request
import json

# 기간 수정 예정
def GetPeriod():
    # print('시작 입력(YYMMDD) :')
    # print('검색할 년도 입력 :(YY)')
    # inputText = input()
    # startDate = "20%s-%s-%s" % (inputText[0:2], inputText[2:4], inputText[4:])
    startDate = "2016-01-01" % inputText
    # startDate = "20%s-%s-%s" % (inputText[0], inputText[1], inputText[2])
    # YY-MM-DD

    # print('종료일 입력(YYMMDD) :')
    # inputText = input()
    # endDate = "20%s-12-31" % (inputText[0:2], inputText[2:4], inputText[4:])
    # endDate = "20%s-12-31" % inputText
    endDate = ""

    timeUnit = "month" # 고정

    return startDate, endDate, timeUnit

def GetKeyword(startDate, endDate, timeUnit):
    print('[조회할 키워드 2개를 입력해주세요.]')
    print('1번째 키워드 입력 :')
    keyWord = "[\"%s\"," % input()

    print('2번째 키워드 입력 :')
    keyWord += "\"%s\"]" % input()

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