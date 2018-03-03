from pyecharts import Pie
import pandas as pd
# 图形界面展示上海地区对爬虫需求的地点分布
# 读取
data = pd.read_csv('zz.csv',usecols=[3])
new_data = data.values
new_data_s = []
for i in new_data:
    new_data_s.append(''.join(i))
# print(new_data_s)

# 统计每一个区域出现的次数
# 集合去重
set1 = set(new_data_s)
print(list(set1))
new_list = list(set1)
# 新建 两个 列表用来保存数据
address = []
count = []

for i in new_list:
    address.append(i)
    # 统计出现的次数
    count.append(new_data_s.count(i))

print(address)
print(count)
# 使用字典来保存结果 用来对比结果是佛真确
# dict1 = {}
# for item in set1:
#     dict1.update({item: new_data_s.count(item)})
# print(dict1)

# 这是实现图形部分 ----饼状图
# 标题
pie = Pie('Python需求地点分布情况- lovlu',title_pos='center')
# legend_top='bottom' 将小标放在下面
pie.add("",address,count,is_label_show=True,legend_top='bottom')
# 做成网页，默认为当前文件夹
pie.render()
# 圆形图

