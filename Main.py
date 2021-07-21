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

    for i in range(2):
        inputValue = input('2개의 키워드를 입력하세요. (ex. 클라우드,cloud)\n')
        DataCrawl.SetKeyWord(inputValue.split(','))

        crawledData = DataCrawl.GetCrawlingResult()          # 1. 크롤링
        refinedData = DataRefine.DataRefining(crawledData)   # 2. 정제
        resultData.append(refinedData)

    DataVisual.PrintInfo(resultData)                            # 3. 시각화

    # 07.21. 신규 추가 ------------------------------
    DataCrawlByDate.query = inputValue # input 재활용
    directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData() # <------------------- 워드 클라우드용 데이터
    DataCrawlByDate.GetExcelResultQuery(directlyCrawledData)

if __name__ == '__main__':
    Main()