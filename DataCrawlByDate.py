import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
from requests.api import request
import re # 정규식용
import time # 시간 측정용
from pandas import DataFrame # Excel 출력용

# 오늘 날짜 값 정제
date = str(datetime.now())
date = date[:date.rfind(' ')]

url = 'https://search.naver.com/search.naver'

requestUrl = ''
maxNewsNum = 0
pages = None
query = ''

def InitVariables():

    global maxNewsNum, requestUrl, pages, query # 전역 변수 사용 선언

    # query = input('검색 키워드를 입력 : ')
    query = query.replace(' ', '+') # 네이버 판정
    query = query.replace(',', '+')

    maxNewsNum = int(input('필요한 뉴스 기사 개수 : '))

    startDate = input('검색 시작일 : (YYYYMMDD)\n') # 20210721
    endDate = input('검색 종료일 : (YYYYMMDD)\n')

    requestUrl = url
    requestUrl += '?sm=tab_hty.top&where=news'
    requestUrl += '&query=%s' % query # 검색어
    requestUrl += '&sm=tab_opt&sort=0&photo=0&field=0&pd=3'
    requestUrl += '&ds=%s.%s.%s' % (startDate[0:4], startDate[4:6], startDate[6:]) # news_url += '&ds=2000.01.01' (시작일)
    requestUrl += '&de=%s.%s.%s' % (endDate[0:4], endDate[4:6], endDate[6:]) # news_url += '&de=2000.12.31' (종료일)
    # 최종 url 주소값 생성

    req = requests.get(requestUrl)
    soup = BeautifulSoup(req.text, 'html.parser')
    pages = soup.find('div', {'class' : 'sc_page_inner'})

def CrawlingByTime():
    # 전역 변수로 url 받기
    url = requestUrl

    totalTime = 0 # 시간 측정용 변수
    sTime = time.time()

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser') # 파싱

    newsResultDict = {} # key : 번호, value : 뉴스 제목, contents : 내용 미리보기
    outerIndex = 0 # 현재 뉴스의 번호 (*** idx를 전역변수로 선언한 이유)
    nowPage = 1

    print('크롤링 중...')

    flag = True
    while outerIndex < maxNewsNum: # idx를 전역변수로 선언한 이유 (누적 카운팅)
        
        '---------- 장기 작업 구간 ----------'
        if flag and (time.time() - sTime) > 6: # 첫 경과 시 출력
            print('\n작업이 길어지고 있습니다. 잠시만 기다려주세요... :)\n')
            flag = False
        '------------------------------------'
        
        table = soup.find('ul', {'class' : 'list_news'})

        '---------- 에러 처리 ----------'
        if table is None:
            print('\n','-'*32,'\n','- [알림] 검색 결과가 없습니다. -','\n','-'*32,'\n')
            break

        liList = table.find_all('li', {'id' : re.compile('sp_nws.*')})
        areaList = [li.find('div', {'class' : 'news_area'}) for li in liList]

        aList = [area.find('a', {'class' : 'news_tit'}) for area in areaList]

        dscList = [area.find('div', {'class' : 'news_dsc'}) for area in areaList]
        wrapList = [dsc.find('div', {'class' : 'dsc_wrap'}) for dsc in dscList]
        contentsList = [wrap.text for wrap in wrapList]

        infoList = [area.find('div', {'class' : 'news_info'}) for area in areaList]
        infoGroupList = [info.find('div', {'class' : 'info_group'}) for info in infoList]
        spanList = [info_group.find('span', {'class' : 'info'}) for info_group in infoGroupList]

        innerIndex = 0
        for n in spanList[:min(len(spanList), maxNewsNum - outerIndex)]:
            newsResultDict[outerIndex] = {'date' : n.text, 'title' : aList[innerIndex].get('title'), 'contents' : contentsList[innerIndex]} 
            outerIndex = outerIndex + 1
            innerIndex = innerIndex + 1

        '---------- 에러 처리 ----------'
        if len(liList) < 10:
            print('\n자료량이 요구량보다 적습니다!\n', outerIndex, '개 출력했습니다.')
            totalTime = (time.time() - sTime)
            return newsResultDict, totalTime

        nowPage = nowPage + 1
        pages = soup.find('div', {'class' : 'sc_page_inner'})

        '---------- 에러 처리 ----------'
        try:
            nextPageUrl = [p for p in pages.find_all('a') if p.text == str(nowPage)][0].get('href')
        except IndexError as ie:
            print('\n자료량이 요구량보다 적습니다!\n', outerIndex, '개 출력했습니다.')
            break

        req = requests.get(url + nextPageUrl)
        soup = BeautifulSoup(req.text, 'html.parser')

    # 현재t - 시작t = 소요t
    totalTime = (time.time() - sTime)
    
    return newsResultDict, totalTime

def GetNewsCrawlingData():
    InitVariables()
    newsResultDict, totalTime = CrawlingByTime()
    print('크롤링 완료')

    ' @ Terminal 결과 출력 - 임시 비활성화'
    # for i in range(len(newsResultDict)):
    #     print('date :', newsResultDict[i]['date'], '\ntitle :', newsResultDict[i]['title'], '\ncontents :', newsResultDict[i]['contents'], '\n')
    print('소요 시간 :', round(totalTime, 2), '초')

    return newsResultDict

def printExcelResult(data):
    dateFrame = DataFrame(data).T
    fileName = '%s의_결과[%s].xlsx' % (query, date)
    dateFrame.to_excel(fileName)
    print('Excel 출력 완료!')

def GetExcelResultQuery(data):
    print('\n','-'*32,'\n','- Excel 결과물 출력 여부 [Y/N] -','\n','-'*32,'\n')
    userInput = input()
    if userInput == 'Y' or userInput == 'y':
        printExcelResult(data) # Excel로 정제 및 출력
    elif userInput == 'N' or userInput == 'n':
        pass
    else:
        print('잘못된 입력입니다.')
    print('종료합니다.\n')