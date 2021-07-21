import DataCrawl
import DataRefine
import DataVisual

def Gradient(ratio):
    pass

def Main():    
    # 출력할 keyWord 입력 받기 <-----------------  
    refinedData = list()
    DataCrawl.SetKeyWord(input('검색어 입력\n').split(','))
    refinedData1 = DataRefine.DataRefining(DataCrawl.GetCrawlingResult())
    DataCrawl.SetKeyWord(input('검색어 입력\n').split(','))
    refinedData2 = DataRefine.DataRefining(DataCrawl.GetCrawlingResult())
    DataVisual.PrintInfo(refinedData1)
    DataVisual.PrintInfo(refinedData2)

if __name__ == '__main__':
    Main()