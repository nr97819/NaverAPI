def Authentication(request):
    clientId = "gKjj14gCwEygk42XREsy"
    clientSecret = "EDB3_6DXf2"
    request.add_header("X-Naver-Client-Id", clientId)
    request.add_header("X-Naver-Client-Secret", clientSecret)
    request.add_header("Content-Type", "application/json")
    return request