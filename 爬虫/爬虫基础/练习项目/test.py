'''
@Author: your name
@Date: 2020-03-19 20:13:09
@LastEditTime: 2020-03-20 15:03:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request库_3.py
'''


# 使用代理
import requests 
from fake_useragent import UserAgent


def main():



    # 构建url
    url = "https://baike.so.com/doc/14824-15354.html"

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


def get_html(url):
    """url---->response"""

    # 构建伪装头,（随机模式）
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 构建代理ip
    proxies = {
        "http": "117.136.106.46"
    }

    # 构建响应
    response = requests.get(url, headers=headers,proxies=proxies)
    
    # 提取内容
    info = response.text
    print(info)
if __name__ == "__main__":
    # get_html("http://www.baidu.com") 
    main()