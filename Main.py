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
    # test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        inputKeyword = input("%d번째 검색할 단어를 입력해 주세요.\n" %(i+1)).split(',') 
        # DataCrawl.SetKeyWord(test[i])
        # listForRecycle.append(str(test[i]))
        DataCrawl.SetKeyWord(inputKeyword)
        listForRecycle.append(str(inputKeyword))

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
        
        visualInfoList = []
        for j in range(2): # 1 : 최상권, 2 : 최하권
            if count % 2 == 0:
                visualInfoList.append('관심도 최상위') # 검색 주제
            else:
                visualInfoList.append('관심도 최하위') # 검색 주제

            for k in range(2): # 1 : 시작일 - 종료일
                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count], 50) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)
                
                visualInfoList.append(listForRecycle[i]) # 검색 주제
                visualInfoList.append(targetDate[count]) # 기간(날짜)
                DataRefine.DataRefining2(directlyCrawledData)
                'to민지님) 위 함수 2번째 인자에, visualInfoList 넣어서 사용하시면 됩니다.'

                count = count + 1

if __name__ == '__main__':
    Main()