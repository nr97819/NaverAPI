import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
from requests.api import request
import re # 정규식용
import time # 시간 측정용
from pandas import DataFrame # Excel 출력용
import os # 파일 경로 지정용

# 오늘 날짜 저장
date = str(datetime.now())
date = date[:date.rfind(' ')]

URL = 'https://search.naver.com/search.naver'
requestUrl = ''
pages = None
query = ''

# Summary:
# 전역 변수 초기화
# param:
# 검색 시작일/종료일
# returns:
# 없음
def InitVariables(startDate, endDate): # default 100
    global requestUrl, pages, query # 전역

    query = query.replace(' ', '+') # 네이버 검색 윤활

    # 최종 url 주소 생성
    requestUrl = URL
    requestUrl += '?sm=tab_hty.top&where=news'
    requestUrl += '&query=%s' % query # 키워드
    requestUrl += '&sm=tab_opt&sort=0&photo=0&field=0&pd=3'
    requestUrl += '&ds=%s.%s.%s' % (startDate[0:4], startDate[4:6], startDate[6:]) # '&ds=2000.01.01' (시작일)
    requestUrl += '&de=%s.%s.%s' % (endDate[0:4], endDate[4:6], endDate[6:]) # '&de=2000.12.31' (종료일)

    req = requests.get(requestUrl)
    soup = BeautifulSoup(req.text, 'html.parser')
    pages = soup.find('div', {'class' : 'sc_page_inner'})

# Summary:
# 크롤링 기간별 작업 대행 (갑)
# param:
# 최대 출력 뉴스 수
# returns:
# 크롤링 결과 전달, 걸린 시간
def CrawlingByTime(maxNewsNum):
    # 전역 변수로 url 받기
    tempUrl = requestUrl

    totalTime = 0
    sTime = time.time()

    req = requests.get(tempUrl)
    soup = BeautifulSoup(req.text, 'html.parser') # 파싱

    newsResultDict = SplitUsableData(soup, maxNewsNum, sTime, tempUrl)

    totalTime = (time.time() - sTime)
    return newsResultDict, totalTime

# Summary:
# 크롤링 기간별 작업 (을)
# param:
# 중간 전달 (soup, maxNewsNum, sTime, tempUrl)
# returns:
# 크롤링 결과
def SplitUsableData(soup, maxNewsNum, sTime, tempUrl):
    print('크롤링 중...')

    newsResultDict = {}
    outerIndex = 0
    nowPage = 1

    flag = True
    while outerIndex < maxNewsNum:
        # 5초 경과시 (1st case만) 안내
        if flag and (time.time() - sTime) > 5:
            print('\n작업이 길어지고 있습니다. 잠시만 기다려주세요... :)\n')
            flag = False
        
        table = soup.find('ul', {'class' : 'list_news'})
        # 에러 처리 (무)
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
        # 에러 처리 (게시수)
        if len(liList) < 10:
            # print('\n자료가 부족합니다.\n', outerIndex, '개 출력되었습니다.')
            print('\n', outerIndex, '개 출력되었습니다.')
            return newsResultDict

        nowPage = nowPage + 1
        pages = soup.find('div', {'class' : 'sc_page_inner'})
        # 에러 처리 (페이지수)
        try:
            nextPageUrl = [p for p in pages.find_all('a') if p.text == str(nowPage)][0].get('href')
        except IndexError as ie:
            # print('\n자료가 부족합니다.\n', outerIndex, '개 출력되었습니다.')
            print('\n', outerIndex, '개 출력되었습니다.')
            break

        req = requests.get(tempUrl + nextPageUrl)
        soup = BeautifulSoup(req.text, 'html.parser')

    return newsResultDict

# Summary:
# 메인에서 크롤링을 위한 호출 (작업 뭉치)
# param:
# '20000101-20010101', 최대 기사 수(기본 100)
# returns:
# 검색 결과
def GetNewsCrawlingData(dateList, maxNewsNum=100):
    startDate, endDate = dateList.split('-')
    InitVariables(startDate, endDate)                       # 초기화
    newsResultDict, totalTime = CrawlingByTime(maxNewsNum)  # 크롤링 (기간별)
    print(maxNewsNum, '개(최대) 출력되었습니다.')
    print('크롤링 완료!')
    print('소요 시간 :', round(totalTime, 2), '초')
    return newsResultDict

# Summary:
# EXCEL 출력 대행 (을)
# param:
# 기간, 파일번호
# returns:
# 없음
def printExcelResult(data, fileNumber):
    dateFrame = DataFrame(data).T
    filePath = os.getcwd() + r'\\NaverAPI\\'
    fileName = filePath + '%s의_결과_%s_%s.xlsx' % (query, fileNumber, date)
    dateFrame.to_excel(fileName)
    print('Excel 파일 출력 완료!\n')

# Summary:
# EXCEL 출력 대행 (갑)
# param:
# 기간, 파일번호 (전달)
# returns:
# 없음
def GetExcelResultQuery(data, fileNumber):
    printExcelResult(data, fileNumber)