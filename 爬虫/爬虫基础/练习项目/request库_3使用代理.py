'''
@Author: your name
@Date: 2020-03-19 20:13:09
@LastEditTime: 2020-03-20 15:00:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request库_3.py
'''


# 使用代理
import requests 
from fake_useragent import UserAgent


def main():


    # 构建url
    url = "https://www.baidu.com/"

    # 创建请求头
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 创建代理IP
    proxies = {
        "http": "http://60.190.23.50"
    }

    # 创建返回
    response = requests.get(url, headers=headers, proxies=proxies)

    # 打印显示
    print(response.text)

if __name__ == "__main__":
    main()  