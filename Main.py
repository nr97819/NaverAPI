import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate
import numpy as np
import CrawlVisual
from ChangeFinder import ChangeFind

def Main():      
    resultData = list()
    refinedInputList = []
    test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        inputKeyword = input("%d번째 검색할 단어를 입력해 주세요.\n" %(i+1)).split(',') 
        ' ----------- 테스팅용 -----------'
        if inputKeyword[0] == '': # Enter 입력 시, 디폴트 적용
            print('디폴트 값 사용\n')
            inputKeyword = test[i]
        ' ---------- ---------- ----------'
        DataCrawl.SetKeyWord(inputKeyword)
        refinedInputList.append(str(inputKeyword[0] + ', ' + inputKeyword[1])) # 2차 crawl을 위해, 정제 및 저장

        # DataCrawl.SetKeyWord(test[i])
        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    targetDate = ChangeFind(resultData).targetDate

    count = 0
    for i in range(2): # 1 : 클라우드, 2 : 클라우드 보안
        print('[알림]', '\n','-'*60,'\n', refinedInputList[i], '에 대한 상세검색을 진행합니다','\n','-'*60,'\n')
        DataCrawlByDate.query = str(refinedInputList[i]) # input 재활용
        # print('[알림]', '\n','-'*66,'\n', str(inputKeyword[i]), '에 대한 상세검색을 진행합니다 -','\n','-'*66,'\n')
        # DataCrawlByDate.query = str(inputKeyword[i]) # input 재활용

        for j in range(2): # 1 : 최상권, 2 : 최하권
            for k in range(2): # 1 : 시작일 - 종료일
                visualInfoList = []
                if j == 0:
                    visualInfoList.append('관심도 최상위') # 검색 주제
                else:
                    visualInfoList.append('관심도 최하위') # 검색 주제

                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count], 50) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)
                
                visualInfoList.append(refinedInputList[i]) # 검색 주제
                # visualInfoList.append(str(inputKeyword[i])) # 검색 주제
                visualInfoList.append(targetDate[count]) # 기간(날짜)
                CrawlVisual.WordData(DataRefine.DataRefining2(directlyCrawledData, visualInfoList))

                count = count + 1

if __name__ == '__main__':
    Main()