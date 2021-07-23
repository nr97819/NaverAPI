import DataCrawl
import DataRefine
import DataCrawlByDate
import numpy as np
import CrawlVisual
from ChangeFinder import ChangeFind
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg

def Main():      
    resultData = list()
    refinedInputList = []
    wc = list()
    titleText = list()

    for i in range(2):
        inputKeyword = input("%d번째 검색할 단어를 입력해 주세요.\n" %(i+1)).split(',') 
        
        DataCrawl.SetKeyWord(inputKeyword)
        refinedInputList.append(str(inputKeyword[0] + ', ' + inputKeyword[1])) # 2차 crawl을 위해, 정제 및 저장
        
        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    targetDate = ChangeFind(resultData).targetDate

    count = 0
    for i in range(2): # 1 : 클라우드, 2 : 클라우드 보안
        print('[알림]', '\n','-'*60,'\n', refinedInputList[i], '에 대한 상세검색을 진행합니다','\n','-'*60,'\n')
        DataCrawlByDate.query = str(refinedInputList[i]) # input 재활용
        for j in range(2): # 1 : 최상권, 2 : 최하권
            for k in range(2): # 1 : 시작일 - 종료일
                visualInfoList = []
                if j == 0:
                    visualInfoList.append('관심도 상위 구간') # 검색 주제
                else:
                    visualInfoList.append('관심도 하위 구간') # 검색 주제

                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count]) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)
                
                visualInfoList.append(refinedInputList[i]) # 검색 주제
                visualInfoList.append(targetDate[count]) # 기간(날짜)
                refinedText = DataRefine.DataRefining2(directlyCrawledData, visualInfoList)
                titleText.append(refinedText)
                wc.append(CrawlVisual.WordData(refinedText))
                count = count + 1
    wcNum = 0
    fig = plt.figure(figsize=(14, 12))
    for wcItems in wc:
        wcNum = wcNum + 1
        ax = fig.add_subplot(2, 4, wcNum)
        ax.set_title(titleText[wcNum - 1][0]['title'] +'  '+ titleText[wcNum - 1][0]['extremum'] +'\n'+ titleText[wcNum - 1][0]['date'], fontsize='8')
        ax.imshow(wcItems,interpolation='bilinear')
        ax.axis('off')
    fig.tight_layout(pad=0)
    plt.show()
    
if __name__ == '__main__':
    Main()