# NaverAPI를 활용한 검색어 동향 추이 분석

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

본 프로젝트는 python 크롤링 학습 과정에서 제작되었습니다.

Your README file is normally the first entry point to your code. It should tell people why they should use your module, how they can install it, and how they can use it. Standardizing how you write your README makes creating and maintaining your READMEs easier. Great documentation takes work!

본 레포지토리에 포함된 항목들:

1. [The specification](spec.md) for how a standard README should look.
2. A link to [a linter](https://github.com/RichardLitt/standard-readme-preset) you can use to keep your README maintained ([work in progress](https://github.com/RichardLitt/standard-readme/issues/5)).
3. A link to [a generator](https://github.com/RichardLitt/generator-standard-readme) you can use to create standard READMEs.
4. [A badge](#badge) to point to this spec.
5. [Examples of standard READMEs](example-readmes/) - such as this file you are reading.

Standard Readme is designed for open source libraries. Although it’s [historically](#background) made for Node and npm projects, it also applies to libraries in other languages and package managers.


## 프로젝트 목차

- [배경 내용](#배경-설명)
- [실행 및 테스트 방법](#실행-및-테스트-방법)
- [결과물](#결과물)

## 배경 설명

Standard Readme started with the issue originally posed by [@maxogden](https://github.com/maxogden) over at [feross/standard](https://github.com/feross/standard) in [this issue](https://github.com/feross/standard/issues/141), about whether or not a tool to standardize readmes would be useful. A lot of that discussion ended up in [zcei's standard-readme](https://github.com/zcei/standard-readme/issues/1) repository. While working on maintaining the [IPFS](https://github.com/ipfs) repositories, I needed a way to standardize Readmes across that organization. This specification started as a result of that.

> Your documentation is complete when someone can use your module without ever
having to look at its code. This is very important. This makes it possible for
you to separate your module's documented interface from its internal
implementation (guts). This is good because it means that you are free to
change the module's internals as long as the interface remains the same.

> Remember: the documentation, not the code, defines what a module does.

~ [Ken Williams, Perl Hackers](http://mathforum.org/ken/perl_modules.html#document)

Writing READMEs is way too hard, and keeping them maintained is difficult. By offloading this process - making writing easier, making editing easier, making it clear whether or not an edit is up to spec or not - you can spend less time worrying about whether or not your initial documentation is good, and spend more time writing and using code.

By having a standard, users can spend less time searching for the information they want. They can also build tools to gather search terms from descriptions, to automatically run example code, to check licensing, and so on.

The goals for this repository are:

1. A well defined **specification**. This can be found in the [Spec document](spec.md). It is a constant work in progress; please open issues to discuss changes.
2. **An example README**. This Readme is fully standard-readme compliant, and there are more examples in the `example-readmes` folder.
3. A **linter** that can be used to look at errors in a given Readme. Please refer to the [tracking issue](https://github.com/RichardLitt/standard-readme/issues/5).
4. A **generator** that can be used to quickly scaffold out new READMEs. See [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme).
5. A **compliant badge** for users. See [the badge](#badge).

## 실행 및 테스트 방법

This is only a documentation package. You can print out [spec.md](spec.md) to your console:

```sh
$ standard-readme-spec
# Prints out the standard-readme spec
```

### 결과물

To use the generator, look at [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme). There is a global executable to run the generator in that package, aliased as `standard-readme`.

### 참여자들

This project exists thanks to all the people who contribute. 
<a href="https://github.com/WonhaWoo/NaverAPI/graphs/contributors"><img src="https://user-images.githubusercontent.com/55518121/144660712-0a05fa2b-de57-4312-85f8-e0a64eecf4a6.png" /></a>

## License

[MIT](LICENSE) © Richard Littauer


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
