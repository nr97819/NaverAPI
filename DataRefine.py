from collections import defaultdict
import re
import json

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
    writePath = r'C:\NaverAPI\NaverAPI\naver_datalab_serch_%s.json' % refinedKeyWord
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData

def tokenize(message):
    message = message.lower()
    all_words = re.findall("[가-힣a-z0-9]+", message)
    return all_words

def count_words(data):
    counts = defaultdict(lambda: 0)
    for message in data:
        for word in tokenize(message):
            counts[word] = counts[word] + 1
    return counts

def DataRefining2(data):
    resultData = []
    for i in range(len(data)):
        resultData.append(data[i]['title']+' '+data[i]['contents'])

    resultWordData = count_words(resultData)

    # 경로는 본인 PC에 맞게 설정
    writePath = r'C:\NaverAPI\NaverAPI\naver_crawl_word.json'
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( resultWordData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return resultWordData