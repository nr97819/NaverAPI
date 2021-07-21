import DataCrawl
import DataRefine
import DataVisual

def Gradient(ratio):
    pass

def Main():    
    # 출력할 keyWord 입력 받기 <-----------------  
    refinedData = list()
    for i in range(2):
        DataCrawl.SetKeyWord(input('검색어 입력\n').split(','))
        refinedData.append(DataRefine.DataRefining(DataCrawl.GetCrawlingResult()))
    DataVisual.PrintInfo(refinedData)

if __name__ == '__main__':
    Main()