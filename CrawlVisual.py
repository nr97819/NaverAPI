
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import numpy as np

def WordData(resultWordData):
    
    #stword = set(STOPWORDS)  # 제외할 단어s
    #stword.add('클라우드')

    image= np.array(pilimg.open(r'C:\LAB\NaverAPI\c.png'))
    
    wc = WordCloud(max_font_size=180,     
                    min_font_size=10,     
                    font_path='C:\\Windows\\Fonts\\HMKMAMI.ttf',
                    background_color='black', 
                    width=1000, height=800,
                    mask= image,
                    colormap ="PuBu"
                    )

    wc.generate_from_frequencies(resultWordData)

    #wc.recolor(color_func= ImageColorGenerator(image))  

    plt.figure(figsize=(8, 5))
    plt.title('검색어', fontsize='15')
    plt.imshow(wc,interpolation='bilinear')
    plt.tight_layout(pad=0)
    plt.axis('off')
    plt.show()
