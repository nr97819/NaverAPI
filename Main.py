import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate
import numpy as np
import CrawlVisual
from ChangeFinder import ChangeFind

def Main():      
    resultData = list()
    test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        inputKeyword = input("%d번째 검색할 단어를 입력해 주세요.\n" %(i+1)).split(',') 
        DataCrawl.SetKeyWord(inputKeyword)
        # DataCrawl.SetKeyWord(test[i])
        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    targetDate = ChangeFind(resultData).targetDate
    print(targetDate)

    count = 0
    for i in range(2): # 1 : 클라우드, 2 : 클라우드 보안
        # print('[알림]', '\n','-'*66,'\n', str(test[i]), '에 대한 상세검색을 진행합니다 -','\n','-'*66,'\n')
        # DataCrawlByDate.query = str(test[i]) # input 재활용
        print('[알림]', '\n','-'*66,'\n', str(inputKeyword[i]), '에 대한 상세검색을 진행합니다 -','\n','-'*66,'\n')
        DataCrawlByDate.query = str(inputKeyword[i]) # input 재활용
        
        for j in range(2): # 1 : 최상권, 2 : 최하권
            if j == 0:
                print('[진행] 관심도 상위 2 구간을 검색합니다.')
            else:
                print('[진행] 관심도 하위 2 구간을 검색합니다.')

            for k in range(2): # 1 : 시작일 - 종료일
                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count], 50) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)
                CrawlVisual.WordData(DataRefine.DataRefining2(directlyCrawledData))
                count = count + 1

if __name__ == '__main__':
    Main()