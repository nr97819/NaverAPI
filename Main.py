import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate
import numpy as np
from ChangeFinder import ChangeFind

def Main():      
    # 출력할 keyWord 입력 받기 <-----------------
    resultData = list()
    inputValue = ''
    listForRecycle = []
    test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        DataCrawl.SetKeyWord(test[i])
        listForRecycle.append(str(test[i]))

        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    # DataVisual.PrintInfo(resultData)
    targetDate = ChangeFind(resultData).targetDate
    print(targetDate)

    count = 0
    for i in range(2): # 1 : 클라우드, 2 : 클라우드 보안
        print('[알림]', '\n','-'*66,'\n',listForRecycle[i], '에 대한 상세검색을 진행합니다 -','\n','-'*66,'\n')
        DataCrawlByDate.query = listForRecycle[i] # input 재활용
        
        for j in range(2): # 1 : 최상권, 2 : 최하권
            if count % 2 == 0:
                print('[진행] 급상승 기간 2곳을 검색합니다.')
            else:
                print('[진행] 급하강 기간 2곳을 검색합니다.')

            for k in range(2): # 1 : 시작일 - 종료일
                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count]) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)

                count = count + 1

if __name__ == '__main__':
    Main()