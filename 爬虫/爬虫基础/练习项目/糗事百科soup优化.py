'''
@Author: your name
@Date: 2020-03-20 23:52:21
@LastEditTime: 2020-03-21 17:33:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\test2.py
'''
import requests
from fake_useragent import UserAgent
import re
import time
from bs4 import BeautifulSoup

def get_html(url):
    """url---->response"""

    # 构建伪装头,（随机模式）
    headers = {
        "User-Agent": UserAgent().random  
    }

    # 构建代理ip
    # proxies = {
    #     "http": "117.136.106.46"
    # }

    # 构建响应
    response = requests.get(url, headers=headers)
    
    # 提取内容
    info = response.text

    return info

def re_html(html):
    """单个网页，标题表达式，内容表达式----->要提取内容的字符串"""

    soup = BeautifulSoup(html, "lxml")
    content = soup.select(".content > p")

    return content

def save_html(name, html):
    """保存到文件，
    字符串-----文件
    """
    with open(name, "a", encoding="utf-8") as f:
        for num in range(8):
            f.write(re_html(html)[num].text + "\n\n")

def main():

    # 输入
    old_url = "http://qiushidabaike.com/index_{}.html"

    # 第一页
    i = 1

    # 拼凑url
    while True:
        new_url = old_url.format(i)


        # 构建单网页抓取函数
        html = get_html(new_url)
        print("正在打印第{}页".format(i) )


        # 判断网页是否结束
        if not html:
            break


        # 提取数据


        # 保存内容
        # name = "第{}页.txt".format(i)
        save_html("段子.txt", html)


        # 暂停一秒
        time.sleep(3)

        i += 1

    print("爬取结束")



if __name__ == "__main__":
    main()