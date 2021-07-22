import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate

def Gradient(ratio):
    pass

def Main():    
    # 출력할 keyWord 입력 받기 <-----------------  
    resultData = list()
    inputValue = ''
    listForRecycle = []

    for i in range(2):
        inputValue = input(i, '번째 그룹의 키워드를 2개 입력하세요. (ex. 클라우드, cloud)\n')
        DataCrawl.SetKeyWord(inputValue.split(','))
        listForRecycle.append(inputValue) # 재활용을 위해 List 사용

        crawledData = DataCrawl.GetCrawlingResult()          # 1. 크롤링
        refinedData = DataRefine.DataRefining(crawledData)   # 2. 정제
        resultData.append(refinedData)

    DataVisual.PrintInfo(resultData)                         # 3. 시각화

    # 07.21. 신규 추가 ------------------------------
    for i in range(2):
        print('[', listForRecycle[i], '에 대한 상세검색 ]')
        DataCrawlByDate.query = listForRecycle[i] # input 재활용
        directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData() # <------------------- 워드 클라우드용 데이터
        DataCrawlByDate.GetExcelResultQuery(directlyCrawledData)

if __name__ == '__main__':
    Main()