import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib
import numpy as np
import ruptures as rpt

fromLocation = r"C:\Windows\Fonts\HMFMPYUN.ttf"
fontName = font_manager.FontProperties(fname=fromLocation).get_name()
matplotlib.rc('font', family=fontName)

def ChangeFind(addrData):
    fig = plt.figure(num="SearchTrend", figsize=(10, 6))
    gs = fig.add_gridspec(2, 1)

    for plotNum in range(2):
        length = addrData[plotNum][0]['len']
        x_label = np.array([])
        y_label = np.zeros((length, 2))

        for item in range(length):
            x_label = np.append(x_label, item)
            y_label[item][plotNum] = round(addrData[plotNum][0]['data'][item]['ratio'], 2)
        
        model = "rbf"
        algo = rpt.Pelt(model=model).fit(y_label[:, plotNum])
        bkps = algo.predict(pen=int(length / 100))
        n_bkps = algo.predict(pen=int(length / 100))
        print(bkps)
        _, curr_ax = rpt.display(y_label[:, plotNum], bkps, n_bkps, num="SearchTrend")
        curr_ax[0].set_position(gs[plotNum].get_position(fig))
        curr_ax[0].set_subplotspec(gs[plotNum])
        plt.title(addrData[plotNum][0]['keyword'])
    plt.show()

def PrintInfo(addrData):
    for plotNum in range(2):
        length = addrData[plotNum][0]['len']
        plt.subplot(211 + plotNum)
        y_label = []
        x_label = []
        
        for i in range(length):
            temp = addrData[plotNum][0]['data'][int(i)]['ratio']
            y_label.append(round(temp, 2))
            x_label.append(i)
        
        date = []               # x_label에 날짜
        for j in range(length):    
            temp2= addrData[plotNum][0]['data'][int(j)]['period']
            if j%50==0:
                date.append(temp2)
 
        plt.xticks(np.arange(0,length,50),date)  # x축 간격 50
        plt.xticks(rotation =7)

        plt.plot(x_label,y_label, 0.7, color='green')

        plt.title(addrData[plotNum][0]['keyword'],fontsize=18,c='b')
        plt.xlabel('기간', c= 'purple')
        plt.ylabel('검색률',c='purple')
        plt.axis([1, length, 0, 100]) 
       
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.subplots_adjust(wspace=0.2, hspace=0.7)
        plt.grid(True, axis='y',linestyle='--',alpha=0.4)  
    plt.show()

    print('''
    -----------------------------------------
    - 정상적으로 통계 파일이 추출되었습니다 -
    -----------------------------------------
    ''')