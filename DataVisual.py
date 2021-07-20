import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

fromLocation = r"C:\Windows\Fonts\malgun.ttf"
fontName = font_manager.FontProperties(fname=fromLocation).get_name()
matplotlib.rc('font', family=fontName)

def PrintInfo(addrData):
    y_label = []
    x_label = list()

    for i in range(addrData[0]['len']):
        temp = addrData[0]['data'][int(i)]['ratio']
        y_label.append(round(temp, 2))
        x_label.append(i)
    
    'ro' 'b' 'bs' 'g' # 빨간점, 파랑, 파란네모, 초록
    # plt.plot(   [1,2,3,4,5,6,7,8,9,10,11,12], 
    #             [list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11]],
    #             0.9, 
    #             color='green')
    plt.plot(   x_label, 
                y_label,
                0.9, 
                color='green')
    plt.xlabel('월별')
    plt.ylabel('검색률')
    
#      plt.bar(
# [1,2,3,4,5,6,7,8,9,10,11,12], 
# [list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11]], 'b') # x도 1부터 시작

    # 표시 범위
    plt.axis([1, addrData[0]['len'], 0, 100]) # x축의 범위 0~10 / y축의 범위 0~20
    plt.show()
    

    print('''
    -----------------------------------------
    - 정상적으로 통계 파일이 추출되었습니다 -
    -----------------------------------------
    ''')