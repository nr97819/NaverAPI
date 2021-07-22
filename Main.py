import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate

def Main():      
    # 출력할 keyWord 입력 받기 <-----------------
    resultData = list()
    inputValue = ''
    listForRecycle = []
    
    test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        # inputValue = input('키워드를 2개 입력하세요. (ex. 클라우드, cloud)\n')
        # DataCrawl.SetKeyWord(inputValue.split(','))
        # listForRecycle.append(inputValue)
        DataCrawl.SetKeyWord(test[i])
        listForRecycle.append(str(test[i]))

        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    # DataVisual.PrintInfo(refinedData)기존 그래프
    DataVisual.ChangeFind(resultData)

    for i in range(2):
        print('[', listForRecycle[i], '에 대한 상세검색 ]')
        DataCrawlByDate.query = listForRecycle[i] # input 재활용
        directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData() # <------------------- 워드 클라우드용 데이터
        DataCrawlByDate.GetExcelResultQuery(directlyCrawledData)
        resultWordData = DataRefine.DataRefining2(directlyCrawledData)

if __name__ == '__main__':
    Main()