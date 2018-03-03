import urllib.request
import urllib.parse
import json
import pandas

# 连接本地是数据库

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0'


for page in (1,5):
    # pn 是页数 爬去的是第一页
    data = {
    'first':'true',
    'pn':page,
    'kd':'python爬虫'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Cookie':'_ga=GA1.2.1536451434.1519973101; _gid=GA1.2.1668550274.1519973101; user_trace_token=20180302144459-39f3cbe5-1de5-11e8-b116-5254005c3644; LGUID=20180302144459-39f3d6db-1de5-11e8-b116-5254005c3644; ab_test_random_num=0; hasDeliver=0; index_location_city=%E4%B8%8A%E6%B5%B7; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22161e5992a8e124-088ba281eb3ae2-4545092c-1049088-161e5992a8fad5%22%2C%22%24device_id%22%3A%22161e5992a8e124-088ba281eb3ae2-4545092c-1049088-161e5992a8fad5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAACBHABBI4769242252314E5F5D4020EE9B291BAC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519973101,1519973187,1519989061; _putrc=7F2BC56D1A7D5D96123F89F2B170EADC; login=true; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; LGSID=20180302204544-9f8dec0d-1e17-11e8-9a4a-525400f775ce; TG-TRACK-CODE=search_code; unick=%E9%83%AD%E4%B9%89%E5%BC%BA; gate_login_token=f04a81a8e402954278f57277a3f3188924c50da62d959ea1c8c82a9b4449ea19; _gat=1; SEARCH_ID=199acff8695c4800a6cfadcbecf65a66; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519996748; LGRID=20180302211904-4772d66b-1e1c-11e8-9a50-525400f775ce',
    'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?oquery=python%E7%88%AC%E8%99%AB&fromSearch=true&labelWords=relative&city=%E4%B8%8A%E6%B5%B7',
    }
    res = urllib.request.Request(url,data,headers=headers)

    response = urllib.request.urlopen(res).read().decode('utf-8')
    response = json.loads(response)
    print(response)



