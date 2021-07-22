from collections import defaultdict
import re
import json
import os
import CrawlVisual         #########################3
# Summary:
# 통합 검색어 트렌드 데이터 정제, 김민지
# param:
# resultData - 정제할 데이터
# returns:
# refinedData - 정제된 데이터

def DataRefining(resultData):
    refinedData = []
    refinedLen = 0

    refinedResult = json.loads(resultData)
    refinedLen = len(refinedResult['results'][0]['data'])
    refinedKeyWord = refinedResult['results'][0]['keywords'][0]

    refinedData.append({'len':refinedLen,
                        'keyword':refinedKeyWord,
                        'data':[]
    })

    for data in refinedResult['results'][0]['data']:
        refinedPeriod = data["period"]
        refinedRatio = data["ratio"]

        refinedData[0]['data'].append({'period' : refinedPeriod,
                            'ratio' : refinedRatio
        })

    # 경로는 본인 PC에 맞게 설정
    writePath = os.getcwd() + "\\NaverAPI\\naver_datalab_serch_%s.json" % refinedKeyWord
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData

def Tokenize(message):
    with open(os.getcwd() + "\\NaverAPI\\stopWords.txt", 'rt',  encoding='UTF8') as file:
        stopWords = file.read()
    stopWords = stopWords.split('\n')
    
    message = message.lower()

    if '멀티 클라우드' in message:
        message = message.replace('멀티 클라우드', '멀티클라우드')
    if '퍼블릭 클라우드' in message:
        message = message.replace('퍼블릭 클라우드', '퍼블릭클라우드')

    allWords = re.findall("[가-힣a-z0-9]+", message)

    for word in allWords:
        for i in stopWords:
            if i in word:
                resultWord = word.replace(i, '')
                allWords[allWords.index(word)] = resultWord
                break

    return allWords

def CountWords(data):
    counts = defaultdict(lambda: 0)

    for message in data:
        for word in Tokenize(message):
            counts[word] = counts[word] + 1

    if '클라우드' in counts:
        counts.pop('클라우드')
    if 'cloud' in counts:
        counts.pop('cloud')

    num = 0
    while num != len(counts):
        if len(list(counts.keys())[num]) <= 1:
            counts.pop(list(counts.keys())[num])
            num = num
        else:
            num = num + 1

    return counts

def DataRefining2(data):
    resultData = []
    for i in range(len(data)):
        resultData.append(data[i]['title']+' '+data[i]['contents'])

    resultWordData = CountWords(resultData)
    CrawlVisual.WordData(resultWordData)     
    # 경로는 본인 PC에 맞게 설정
    writePath = os.getcwd() + "\\NaverAPI\\naver_crawl_word.json"
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( resultWordData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return resultWordData