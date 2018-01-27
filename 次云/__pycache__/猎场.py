import importlib
import sys
importlib.reload(sys)

import re
import requests
import codecs
import time
import random
from bs4 import BeautifulSoup

absolute="https://movie.douban.com/subject/26322642/comments"
absolute_url="https://movie.douban.com/subject/26322642/comments?start=20&limit=20&sort=new_score&status=P&percent_type="
url="https://movie.douban.com/subject/26322642/comments?start={}&limit=20&sort=new_score&status=P&percent_type="
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Connection':'keep-alive'}

def get_data(html):
    soup=BeautifulSoup(html,'html.parser')
    comment_list = soup.select('.comment > p')
    #print(comment_list)
    date_nodes = soup.select('.comment-time')
    #print( date_nodes)
    next_page= soup.select('#paginator > a')[2].get('href')

    return comment_list,next_page,date_nodes
#if __name__ == '__main__':

    ########先登录豆瓣，把cookie复制放在cookie.txt
    f_cookies = open('D:/cookies.txt', 'r')
    cookies = {}
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    html = requests.get(absolute_url, cookies=cookies, headers=header).content


    # print html
    comment_list = []
    # 获取评论
    comment_list, next_page,date_nodes= get_data(html)
    soup = BeautifulSoup(html, 'lxml')
    comment_list = []
    while (next_page != []):  #查看“下一页”的A标签链接
        #print(absolute + next_page)
        html = requests.get(absolute + next_page, cookies=cookies, headers=header).content
        soup = BeautifulSoup(html, 'lxml')
        comment_list, next_page,date_nodes = get_data(html)


        with open(u"comments.txt", 'a+')  as f:
            for node in comment_list:
                comment = node.get_text().strip().replace("\n", "")
                print(comment)
                f.writelines(comment+ r'\n')
        time.sleep(1 + float(random.randint(1, 100)) / 20)


    import numpy as np
    from snownlp import SnowNLP
    import matplotlib.pyplot as plt

    comment = []
    with open('comments.txt', mode='r') as f:
        rows = f.readlines()
        for row in rows:
            if row not in comment:
                comment.append(row.strip('\n'))


    def snowanalysis(self):
        sentimentslist = []
        for li in self:
            s = SnowNLP(li.decode('utf-8'))
            print(li)
            print(s.sentiments_)
            sentimentslist.append(s.sentiments)
        plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
        plt.show()


    if __name__ == '__main__':
        snowanalysis(comment)

