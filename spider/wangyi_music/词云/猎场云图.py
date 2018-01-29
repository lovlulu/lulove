import importlib  #画图的包
import sys
from scipy.misc import imread
importlib.reload(sys)#我不知道这是你干嘛的

from wordcloud import WordCloud,STOPWORDS#要安装wordcloud库


import jieba.analyse           # 导入结巴分词
import numpy as np             # numpy

from PIL import Image              # 图片处理库PIL
import matplotlib.pyplot as plt



def handle(filename, stopword):#文件处理函数
    with open(filename, 'rb') as f:#打开文件 注意这里是可以读成 rb 二进制的

        data = f.read()
        print(data)

    wordlist = jieba.analyse.extract_tags(data, topK=300)   # 分词，取词频统计后的排名前400的词
    wordStr = " ".join(wordlist)
    print(wordStr)

    hand = np.array(Image.open('wang_white.png'))    # 打开一张图片（随便一张图片就行），词语以图片形状为背景分布
    #下面是化云图的参数设置，画布啊啥的，如果需要学习，建议每一个参数百度一下含义
    my_cloudword = WordCloud(
        # wordcloud参数配置
        width=1024,#画布的宽度
        height=768,#画布的长度
        background_color = 'white',   # 背景颜色 一般都是 白色
        mask = hand,                  # 背景图片
        max_words = 300,              # 最大显示的字数
        stopwords = stopword,         # 停用词
        max_font_size = 80,           # 字体最大值
        font_path='simsun.ttc',  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        random_state=5,  # 设置有多少种随机生成状态，即有多少种配色方案
    )

    my_cloudword.generate(wordStr)          # 生成图片
    my_cloudword.to_file('Leehom.png')    # 保存
    plt.imshow(my_cloudword)  # 显示词云图
    plt.axis('off')  # 是否显示x轴、y轴下标

    plt.show()  # 显示   --------------------------------这个地方有改动

if __name__ == '__main__':


    handle('yiran2.txt', STOPWORDS) #你觉得困困难的部分应该是词的部分，随便一个文本的TXT就行了。你可以简单的复制一段话到txt文件就可以了。



