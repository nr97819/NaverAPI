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
    writePath = r'C:\LAB\NAVERAPI\naver_datalab_serch_%s.json' % refinedKeyWord
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False,
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData