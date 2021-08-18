import os
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import numpy as np

def WordData(resultWordData):
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
        wc.generate_from_frequencies({"None": 1})
    # wc.recolor(color_func= ImageColorGenerator(backImage))
    # fig = plt.figure(figsize=(14, 12), facecolor="white")
    # plt.title(titleText['title'] +'  '+ titleText['extremum'] +'\n'+ titleText[0]['date'], fontsize='10')
    # plt.imshow(wc,interpolation='bilinear')
    # plt.axis('off')
    # plt.tight_layout(pad=0)
    # plt.show()
    # fig.savefig(os.getcwd() + r'/static/%s.png' % titleText[0]['date'])
    return(wc)
