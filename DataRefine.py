def DataRefining(resultData):
    refinedData = json.loads(resultData)
    # 경로는 본인 PC에 맞게 설정
    writePath = r'C:/NaverAPI/NaverAPI/search_naver_data.json'
    with open(writePath, 'w', encoding='utf-8') as filedata:
        rJson = json.dumps( refinedData, 
                            indent=4,
                            sort_keys=False, # 오히려 섞임
                            ensure_ascii=False )
        filedata.write(rJson)
    return refinedData
