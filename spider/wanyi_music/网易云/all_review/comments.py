# import EncryptUtil
import json
import requests
import time
# import Logger
import base64
from  Crypto.Cipher import AES
import os

# logger = Logger.Log()

def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:size]

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
    return format(rs, 'x').zfill(256)

def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    reTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return reTime

class Crawler(object):

    def __init__(self,id):
        # modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
        # pubKey = '010001'
        self.secKey = createSecretKey(16)

        # self.encSecKey = EncryptUtil.rsaEncrypt(self.secKey, pubKey, modulus)
        self.encSecKey = "6936dbe0cf54234c7e4467d43ae0cb89b5885482a4a2901acbfa37c9cab7a8a8d0a6098a5d21af7a79f5b4b3b40568a86e45c256ee6e0c99c256826123569062d6ee84b36876f5b0fadeba180a947cd68c467197743f6e2c319cfe62f5a521b1a70a6b4c660c29e74972645ac40e74aa5be088dd292f25391c54900a5b59f67c"

        self.musicId = id
        self.requestUrl = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%d/"%int(id)

        self.headers = {
        # 'Host': 'music.163.com',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '484',
        # 'Cache-Control': 'max-age=0',
        # 'Origin': 'http://music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        # 'Accept': '*/*',
        # 'DNT': '1',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        # 'Cookie': 'JSESSIONID-WYYY=b66d89ed74ae9e94ead89b16e475556e763dd34f95e6ca357d06830a210abc7b685e82318b9d1d5b52ac4f4b9a55024c7a34024fddaee852404ed410933db994dcc0e398f61e670bfeea81105cbe098294e39ac566e1d5aa7232df741870ba1fe96e5cede8372ca587275d35c1a5d1b23a11e274a4c249afba03e20fa2dafb7a16eebdf6%3A1476373826753; _iuqxldmzr_=25; _ntes_nnid=7fa73e96706f26f3ada99abba6c4a6b2,1476372027128; _ntes_nuid=7fa73e96706f26f3ada99abba6c4a6b2; __utma=94650624.748605760.1476372027.1476372027.1476372027.1; __utmb=94650624.4.10.1476372027; __utmc=94650624; __utmz=94650624.1476372027.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        }

    def getComment(self, offset):
        text = {
            'username': "",
            'password': "",
            'rememberLogin': 'true',
            'offset': offset
        }
        text = json.dumps(text)
        encText = aesEncrypt(aesEncrypt(text, self.nonce), self.secKey)
        data = {
            'params': encText,
            'encSecKey': self.encSecKey
        }
        res = requests.post(self.requestUrl,headers=self.headers, data=data)
        jsonData = res.json()
        self.databaseSave(jsonData)
        # return int(jsonData["total"])


    def process(self, offset):
        # if offset == -1:
        #     return
        # off = offset
        # total = self.getComment(off)
        # while off < 50:
        #      off += 10
        #      self.getComment(off)
        if offset ==1:
            for offset in range(5):
                self.getComment(offset*10)


def main():

    c = Crawler(523251118)
    c.process(1)

if __name__ == '__main__':
    main()