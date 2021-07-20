from datetime import date, datetime # 현재 시각 반환 라이브러리

date = str(datetime.now())
date = date[:date.rfind(' ')]

# 기간 수정 예정
def GetPeriod():
    startDate = "2016-01-01"
    endDate = date # 금일
    timeUnit = "week" # 고정

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

