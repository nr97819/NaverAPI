import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib
import numpy as np
import ruptures as rpt
import os
# fromLocation = os.getcwd() + r"/flask/H2GTRM.TTF"
fromLocation = os.getcwd() + r"/H2GTRM.TTF" 
fontName = font_manager.FontProperties(fname=fromLocation).get_name()
matplotlib.rc('font', family=fontName)
class ChangeFind:
    targetDate = list()
    def __init__(self, addrData):
        self.addrData = addrData
        fig = plt.figure(num="SearchTrend", figsize=(10, 6))
        gs = fig.add_gridspec(2, 1)

        for plotNum in range(2):
            length = addrData[plotNum][0]['len']
            findValue = addrData[plotNum][0]['data']
            x_label = np.array([])
            y_label = np.zeros((length, 2))
            bkpsWidth = list()
            xDate = []
            for item in range(length):
                x_label = np.append(x_label, item)
                y_label[item][plotNum] = round(addrData[plotNum][0]['data'][item]['ratio'], 2)
            
                temp = addrData[plotNum][0]['data'][int(item)]['period']
                if item % 50 == 0:
                    xDate.append(temp)
            
            model, n_bkps = "l2", 15
            algo = rpt.Binseg(model=model).fit(y_label[:, plotNum])
            n_bkps = algo.predict(n_bkps)
            for i in range(len(n_bkps) - 1):
                bkpsWidth.append(n_bkps[i + 1] - n_bkps[i])
            minTwo = sorted(range(len(bkpsWidth)), key=lambda i: bkpsWidth[i])[-2:]
            maxTwo = sorted(range(len(bkpsWidth)), key=lambda i: bkpsWidth[i])[:2]
            self.targetDate.append(findValue[n_bkps[maxTwo[0]] - 1]["period"].replace('-', '') + '-' + findValue[n_bkps[maxTwo[0]]]["period"].replace('-', ''))
            self.targetDate.append(findValue[n_bkps[maxTwo[1]] - 1]["period"].replace('-', '') + '-' + findValue[n_bkps[maxTwo[1]]]["period"].replace('-', ''))
            self.targetDate.append(findValue[n_bkps[minTwo[0]] - 1]["period"].replace('-', '') + '-' + findValue[n_bkps[minTwo[0]]]["period"].replace('-', ''))
            self.targetDate.append(findValue[n_bkps[minTwo[1]] - 1]["period"].replace('-', '') + '-' + findValue[n_bkps[minTwo[1]]]["period"].replace('-', ''))

            _, curr_ax = rpt.display(y_label[:, plotNum], n_bkps, num="SearchTrend")
            curr_ax[0].set_position(gs[plotNum].get_position(fig))
            curr_ax[0].set_subplotspec(gs[plotNum])
            curr_ax[0].set_xticks(np.arange(0, length, 50))
            curr_ax[0].set_xticklabels(xDate)
            curr_ax[0].set_xlabel('기간')
            curr_ax[0].set_ylabel('검색률')
            plt.title(addrData[plotNum][0]['keyword'], fontsize=16, c='indigo', weight='bold')
        plt.tight_layout()
        fig.savefig(os.getcwd() + r'/static/trend.png')
        fig = plt.clf()
        # plt.show()