import requests, json, time, hmac, hashlib, base64, urllib.parse, os, requests, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
Csdn签到和抽奖
'''


class Csdn:
    def __init__(self):
        self.headers = {
            'content-type': 'application/json;charset=UTF-8',
            'cookie': "",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4483.0 Safari/537.36'
        }
        self.data = {
            "ip": "",
            "platform": "pc-my",
            "product": "pc",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4483.0 Safari/537.36",
            "username": USERNAME,
            "uuid": ""
        }

    def draws(self):
        self.headers[
            'cookie'] = COOKIE_DRAW
        self.data['uuid'] = '10_19718702780-1615518137009-545439'
        res = requests.post('https://me.csdn.net/api/LuckyDraw_v2/goodLuck', headers=self.headers, data=self.data)
        data_draw = json.loads(res.text)
        if data_draw['code'] == 200:
            return data_draw['data']
        else:
            return '抽奖失败'

    def signed(self):
        self.headers[
            'cookie'] = COOKIE_SIGNED
        self.data['uuid'] = '10_10213081380-1623757365901-112902'
        res = requests.post('https://me.csdn.net/api/LuckyDraw_v2/signIn', headers=self.headers, data=self.data)
        return json.loads(res.text)


if __name__ == "__main__":
    COOKIE_DRAW = os.environ["COOKIE_DRAW"]  # 点击签到后在控制台从heard里面找到COOKIE
    COOKIE_SIGNED = os.environ["COOKIE_SIGNED"]  # 点击签到后在控制台从heard里面找到COOKIE
    USERNAME = os.environ["USERNAME"]  # 这里是’CSDN‘的用户名，链接后面的
    QQ_SEND = os.environ['QQ_SEND']  # qq发件人信息格式  邮箱+smtp码 比如：iui9@qq.com+********(加号为分隔符)
    QQ_ACCEPT = os.environ['QQ_ACCEPT']  # qq收件人邮箱地址
    t = str(Csdn().draws())
    r = str(Csdn().signed())
    if len(QQ_ACCEPT) != 0:
        Csdn().QQ_notice()
