import os
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import numpy as np

def WordData(resultWordData):
    #stword = set(STOPWORDS)  # 제외할 단어s
    #stword.add('클라우드')

    image= np.array(pilimg.open(os.getcwd() + "\\NaverAPI\\06-Source Code\\c.png"))
    
    wc = WordCloud(max_font_size=180,     
                    min_font_size=10,     
                    font_path='C:\\Windows\\Fonts\\HMKMAMI.ttf',
                    background_color='black', 
                    width=1000, height=800,
                    mask= image,
                    colormap ="PuBu"
                    )
    try:
        wc.generate_from_frequencies(resultWordData[0]['data'])
    except:
        wc.generate_from_frequencies({"None": 1})
    #wc.recolor(color_func= ImageColorGenerator(image))  
    # plt.figure(figsize=(8, 6))
    # plt.title(resultWordData[0]['title'] +'  '+ resultWordData[0]['extremum'], fontsize='15')
    # plt.annotate(resultWordData[0]['date'], xy=(318,60), xycoords='figure pixels',fontsize='10')
    # plt.imshow(wc,interpolation='bilinear')
    # plt.tight_layout(pad=0)
    # plt.axis('off')
    # plt.show()
    return(wc)
