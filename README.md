# NaverAPI를 활용한 검색어 동향 추이 분석

본 프로젝트는 python 크롤링 학습 과정에서 제작되었습니다.

본 레포지토리에 포함된 항목들:

## 프로젝트 목차

- [배경 내용](#배경-설명)
- [실행 및 테스트 방법](#실행-및-테스트-방법)
- [결과물](#결과물)

## 배경 설명

> 프로젝트 선정 배경

네이버 통합 검색어 트렌드 기준 2020년 11월 초 클라우드에 대한 관심이 급증함
 
하지만 클라우드 보안에 관한 관심은 2019년 2월 경, 클라우드에 관한 관심이 저점일 때 가장 높았음

상관관계를 분석하여 클라우드 보안 컨설팅 / 마케팅에 유의미한 데이터로 활용하고자 주제를 선정함.

> 프로젝트 목적

<클라우드>, <클라우드 보안> 각 키워드의 트렌드를 조사하고 급증/급감 시 전후 1개월간 뉴스 데이터를 수집한 후, 
각 뉴스의 제목, 본문에 어떤 키워드들이 어떤 빈도로 언급되었는지 추출하여 시각화 한다.

- Python(BeautifulSoup)을 통해 Naver API 통합 검색어 트렌드, 관심 급증/급감 구간 뉴스 데이터를 추출한다.
- 클라우드, 클라우드 보안 각각의 트렌드 데이터를 날짜별로 정제, 구간별 뉴스 데이터를 단어별로 정제한다.
- Pandas를 활용하여 정제된 트렌드 데이터를 그래프로 나타내고 뉴스 키워드를 Word Cloud로 시각화한다.
- 클라우드, 클라우드 보안에 대한 관심이 급증/급감할 시점에 자주 등장한 키워드를 분류하여 보관한다.
- 향후 뉴스에 해당 키워드가 등장할 경우 실제로 트렌드 변화가 있는지 확인하고 모델을 수정한다.

1. NaverAPI 검색어 트렌드 그래프와 검색어 워드 클라우드를 웹에서 확인할 수 있도록 구현하였다
2. Docker + Docker 즉 Docker Compose를 사용하여 Web, Was 각각의 컨테이너를 빌드하였다. Web은 nginx 1.17.4를, Was는 flask를 사용해 구축하였으며 
3. uWSGI를 Web, Was간 인터페이스로 선정하였다.
4. Web컨테이너와 uWSGI는 지정된 포트로, uWSGI와 Was는 소켓 통신한다.
5. UI/UX를 향상시키기 위해 CSS, Javascript를 사용하였다. (상세한 건 다음 페이지에서 직접 보면서 알아보자)

## 실행 및 테스트 방법

아래 디렉토리로 이동 후, 도커 컴포즈 실행

EC2 인스턴스 구성
```sh
git init
git remote add origin https://github.com/nr97819/NaverAPI.git
git pull origin main

cd 06-Source Code/Module02/docker-compose.yml
docker-compose up -d --build
```

### 결과물

<a href="https://github.com/nr97819/NaverAPI/blob/main/07-%EA%B2%B0%EA%B3%BC%EB%AC%BC/Module02/Module02_result.pdf" />프로젝트 결과물 캡처 파일</a>

### 참여자들

본 프로젝트에 참여한 조원들<br/>
<a href="https://github.com/WonhaWoo/NaverAPI/graphs/contributors"><br/>
<img src="https://user-images.githubusercontent.com/55518121/144660712-0a05fa2b-de57-4312-85f8-e0a64eecf4a6.png" /></a>

## License

[SK infosec Academy]

# 모듈1: Naver Search Trend API
    # Python version : 3.8.10
    # imported library
        # Main : numpy, CrawlVisual, matplotlib, WordCloud, PIL
        # DataAuth : .
        # DataCrawl : typing, datetime, urllib
        # DataCrawlByDate : requests, bs4, datetime, re, time, pandas, os
        # DataRefine : defaultdict, re, json, os
        # ChangeFinder : matplotlib, numpy, ruptures
        # CrawlVisual : os, WordCloud, PIL, matplotlib, numpy

# 모듈2: Naver Search Trend API + Docker Compose
    # Python version : 3.8.10
    # Docker version : 20.10.7
    # Docker Compose version : 2.0.0-beta.6
    # imported library
        # Main : numpy, CrawlVisual, matplotlib, WordCloud, PIL
        # DataAuth : .
        # DataCrawl : typing, datetime, urllib
        # DataCrawlByDate : requests, bs4, datetime, re, time, pandas, os
        # DataRefine : defaultdict, re, json, os
        # ChangeFinder : matplotlib, numpy, ruptures
        # CrawlVisual : os, WordCloud, PIL, matplotlib, numpy
        # run: googletrans, flask
