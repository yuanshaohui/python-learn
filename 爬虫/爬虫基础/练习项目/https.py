'''
@Author: your name
@Date: 2020-03-18 23:28:15
@LastEditTime: 2020-03-18 23:30:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\https.py
'''
from urllib.request import urlopen
from urllib.request import Request
from random import choice
from urllib.parse import quote

def main():
    # 发送请求
    url = "https://www.12306.cn/index/index.html"

    # 伪装访问身份
    # 构建伪装头代码池子
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36","Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11","Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"]
    headers = {
        "User-Agent": choice(user_agent)
    }

    # 构造请求request
    request = Request(url, headers=headers)

    # 构造response对象
    response = urlopen(request)

    # 读取内容
    info = response.read()

    # 打印内容
    print(info.decode())


if __name__ == "__main__":
    main()