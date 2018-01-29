import urllib.request
import re
import threading
from queue import Queue



class Neurology(object):
    def __init__(self):
        # self.header = ('User-Agent',
        #                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
        self.total_url_queue = Queue() # 总的200页的链接池
        self.url_queue = Queue()  # 每一页 里面的20 给链接池
        self.content_queue = Queue()  # 内容池

    def url_list(self):
        # 得到200 个页面的URL 并且 放到  通信池
        url = 'http://www.120ask.com/list/xxgnk/all/%s/'
        for num in range(1,201):
            print(url%num)
            self.total_url_queue.put(url%num)

    def page_url(self):
        # 获得每一页内容20条的链接 并放到 url_queue 池
        while self.total_url_queue.not_empty:
            url = self.total_url_queue.get()
            res = urllib.request.Request(url)
            res.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
            response = urllib.request.urlopen(res).read().decode('utf-8')
            url_list = re.findall(r'class="q-quename" href="(.*?)"', response, re.S)
            for url in url_list:
                self.url_queue.put(url) # 添加到通信池
            self.total_url_queue.task_done() # 取出后 给通信池返回一个消息 为了配合join使用

    def get_content(self):
        # 取出每一个具体内容的链接 得到内容
        # url = 'http://www.120ask.com/question/72070551.htm'
        while self.url_queue.not_empty:
            url = self.url_queue.get()
            res = urllib.request.Request(url)
            res.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
            response = urllib.request.urlopen(res).read().decode('utf-8')
            content = re.search(r"class='crazy_new'>(.*?)</span>(.*?)</p>", response, re.S).group(2)
            content = content.replace(' ', '') + '\n'
            self.content_queue.put(content)
            self.url_queue.task_done()

    def write_content(self):
        # 写入内容
        while self.content_queue.not_empty:
            content = self.content_queue.get()
            print(content)
            with open('心血管内科.txt','a') as f:
                f.write(content)
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        thread_url = threading.Thread(target=self.url_list)
        thread_list.append(thread_url)
        # 发送网络请求
        for i in range(10):
            thread_parse = threading.Thread(target=self.page_url)
            thread_list.append(thread_parse)
        # 提取数据
        for i in range(10):
            thread_get_content = threading.Thread(target=self.get_content)
            thread_list.append(thread_get_content)
        # 保存
        thread_save = threading.Thread(target=self.write_content)
        thread_list.append(thread_save)
        for t in thread_list:
            t.setDaemon(True)  # 为每个进程设置为后台进程，效果是主进程退出子进程也会退出
            t.start()  # 为了解决程序结束无法退出的问题

        self.total_url_queue.join()
        self.url_queue.join()  # 让主线程等待，所有的队列为空的时候才能退出
        self.content_queue.join()


if __name__ == '__main__':
    xiaoqiang = Neurology()
    xiaoqiang.run()

