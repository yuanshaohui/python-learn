'''
@Author: your name
@Date: 2020-03-20 10:58:47
@LastEditTime: 2020-03-20 15:05:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\糗事百科案例.py
'''
import requests
from fake_useragent import UserAgent
import re
import time

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

def re_html(html, str_title, content):
    """单个网页，标题表达式，内容表达式----->要提取内容的字符串"""

    # title = re.findall(r"{}".format(str_title), html)
    content = re.findall(r"{}".format(content), html)
    return content

def save_html(name, content):
    """保存到文件，
    字符串-----文件
    """
    with open(name, "a", encoding="utf-8") as f:
        for i in content:
            f.write(i + "\n\n\n")

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


        # 构建正则函数
        str_title = '<span class="title"><a target="_blank" href=".*?">(.*?)</a></span>'
        # content = '<dd class="content">\s*?<p>(.+)</p>'
        content = '<dd class="content">\s*<p>\s*(.+)\s*</p>\s*'
        content = re_html(html, str_title, content)


        # 保存内容
        # name = "第{}页.txt".format(i)
        save_html("段子.txt", content)


        # 暂停一秒
        time.sleep(3)

        i += 1

    print("爬取结束")



if __name__ == "__main__":
    main()