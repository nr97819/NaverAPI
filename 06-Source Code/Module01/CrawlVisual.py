from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import numpy as np
workDir = "C:\\NaverAPI\\06-Source Code\\Module01\\"

def WordData(resultWordData):
    backImage = pilimg.open(workDir + "cloudShape.png").convert("RGBA")
    x, y = backImage.size
    mask = pilimg.new("RGBA", backImage.size, (255, 255, 255))
    mask.paste(backImage, (0, 0, x, y), backImage)
    mask = np.array(mask)
    wc = WordCloud(max_font_size = 180,     
                    min_font_size = 10,     
                    font_path = 'C:\\Windows\\Fonts\\HMKMAMI.ttf',
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
    return(wc)
