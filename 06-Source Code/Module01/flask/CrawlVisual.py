import os
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import numpy as np

def WordData(resultWordData, count, titleText):
    backImage = pilimg.open(os.getcwd() + r"/cloudShape.png").convert("RGBA")
    x, y = backImage.size
    mask = pilimg.new("RGBA", backImage.size, (255, 255, 255))
    mask.paste(backImage, (0, 0, x, y), backImage)
    mask = np.array(mask)
    wc = WordCloud(max_font_size = 180,     
                    min_font_size = 10,     
                    font_path = os.getcwd() + r"/H2GTRM.TTF" ,
                    background_color ='white', 
                    # width=800, height=800,
                    mask = mask,
                    # colormap = "PuBu"
                    colormap = "winter"
                    )
    try:
        wc.generate_from_frequencies(resultWordData[0]['data'])
    except:
        wc.generate_from_frequencies({"Not Enough Results": 1})
    fig = plt.figure(figsize=(10, 10), facecolor="white")
    plt.title(titleText['title'] +'  '+ titleText['extremum'] +'\n'+ titleText['date'], fontsize='24')
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    # plt.show()
    fig.savefig(os.getcwd() + r'/static/%s.png' % count)
    plt.clf()
    return(wc)
