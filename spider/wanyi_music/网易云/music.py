import urllib.request
import urllib.parse
import json
import pandas

# 不同的ID  对应不同的歌曲
url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_25642129?csrf_token="
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
# data 是可以通用的 但是 也是 后台抓取的
data = {"params":"x3ZEdZRzjR0zIecAMSpedaIhLWEn3QJlQvIJV4WQR/P+U8yNHB0YJfP/SeZcJhuKRltkiDAqdUEc3zeIDLahQKrV255ZUGeCG6ylBqrxB/7w4eAlGhev/ykmxuM4377n9lwCqWcQUcXwLFg7dVeRz4ENDRxE2EV1Dizi+8CRQfrnCGupvoU2pAYo3/OvD6Cwy8TbQ0vBi6tocGvYtKWhdjhV0Ovd3QToNsfF66ipsKo=",
"encSecKey":"6936dbe0cf54234c7e4467d43ae0cb89b5885482a4a2901acbfa37c9cab7a8a8d0a6098a5d21af7a79f5b4b3b40568a86e45c256ee6e0c99c256826123569062d6ee84b36876f5b0fadeba180a947cd68c467197743f6e2c319cfe62f5a521b1a70a6b4c660c29e74972645ac40e74aa5be088dd292f25391c54900a5b59f67c"
}
data = urllib.parse.urlencode(data).encode('utf-8')
res = urllib.request.Request(url,data=data,headers=headers)
response = urllib.request.urlopen(res).read().decode('utf-8')
# print(response)
# 把爬取的页面相应  转换为python中的字典
html = json.loads(response)
# 打印后还是一个大大的字典 里面嵌套了很多的小字典
users_dict = html["hotComments"]

# 创建一个列表 给下面创建的字典使用
new_list = []
# 遍历这个大字典 取出姓名和该人的评论
for user_dict in users_dict:
    new_dict = {}
    new_dict['name'] = user_dict['user']['nickname']
    new_dict['review'] = user_dict['content']
    new_list.append(new_dict)
print(new_list)
# 使用pandas 保存数据
df = pandas.DataFrame(new_list)
df.to_excel('依然爱你.xlsx')