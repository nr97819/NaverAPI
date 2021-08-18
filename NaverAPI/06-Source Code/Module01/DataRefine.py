from collections import defaultdict
import re
import json
import os
workDir = "C:\\NaverAPI\\NaverAPI\\06-Source Code\\"

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

    writePath = os.getcwd() + "\\NaverAPI\\06-Source Code\\naver_datalab_serch_%s.json" % refinedKeyWord
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData

# Summary:
# 뉴스 데이터 자연어 처리, 김민지
# param:
# message - 자연어 처리할 문장
# returns:
# allWords - 자연어 처리된 문장
def Tokenize(message):
    with open(os.getcwd() + "\\NaverAPI\\06-Source Code\\stopWords.txt", 'rt',  encoding='UTF8') as file:
        stopWords = file.read()
    stopWords = stopWords.split('\n')
    
    message = message.lower()

    if '멀티 클라우드' in message:
        message = message.replace('멀티 클라우드', '멀티클라우드')
    if '퍼블릭 클라우드' in message:
        message = message.replace('퍼블릭 클라우드', '퍼블릭클라우드')

    allWords = re.findall("[가-힣a-z0-9]+", message)

    # 불용어 처리
    for word in allWords:
        for stop in stopWords:
            if word.endswith(stop):
                resultWord = word.replace(stop, '')
                allWords[allWords.index(word)] = resultWord
                break

    return allWords

# Summary:
# 뉴스 데이터 단어 빈도수 추출, 김민지
# param:
# data - 단어 빈도수 추출할 뉴스 데이터
# returns:
# counts - 단어 빈도수 추출된 뉴스 데이터
def CountWords(data, title):
    counts = defaultdict(lambda: 0)

    for message in data:
        for word in Tokenize(message):
            counts[word] = counts[word] + 1

    exList = re.split(', | ', title)
    
    # 검색어와 같은 단어 제거
    for word in exList:
        if word in counts:
            counts.pop(word)
        else:
            pass
    
    NUM = 0
    # 단어 길이가 1보다 작거나 같은 단어 제거
    while NUM != len(counts):
        if len(list(counts.keys())[NUM]) <= 1:
            counts.pop(list(counts.keys())[NUM])
            NUM = NUM
        else:
            NUM = NUM + 1

    return counts

# Summary:
# 뉴스 데이터 정제, 김민지
# param:
# data, info - 정제할 데이터, 데이터 정보
# returns:
# resultWordData - 정제된 데이터
def DataRefining2(data, info):
    resultData = []
    resultWordData = []

    for i in range(len(data)):
        resultData.append(data[i]['title']+' '+data[i]['contents'])

    resultWordData.append({'title':info[1],
                        'date':info[2],
                        'extremum':info[0],
                        'data':CountWords(resultData, info[1])
    })

    writePath = os.getcwd() + "\\NaverAPI\\06-Source Code\\naver_crawl_word_%s_%s_%s.json" % (info[1], info[2], info[0])
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( resultWordData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return resultWordData