'''
@Author: your name
@Date: 2020-03-21 20:01:45
@LastEditTime: 2020-03-21 20:53:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\起点网排行.py
'''

import requests
from fake_useragent import UserAgent
from lxml import etree  # 将字符串转成lxml可以解析的格式
import time

def get_html(url):
    """url----->str"""

    # 构建伪装头
    headers = {
        "User-Agent": UserAgent().random
    }

    # 构建response响应
    response = requests.get(url, headers=headers)
    print(type(response.text))

    return response.text

def main():
    url = "https://www.qidian.com/rank/yuepiao?page=1"

    # 获取页面
    str = get_html(url)

    # 获取可被lxml解析的格式
    e = etree.HTML(str)

    # 解析(以列表的格式返回)
    book_name = e.xpath('//h4/a/text()')
    author = e.xpath('//p[@class="author"]/a[1]/text()')

    # print(book_name)
    # print(author)

    # 第一种遍历方法
    # for num in range(len(book_name)):
    #     print(book_name[num] + "<---->" + author[num])

    # 第二种遍历方法: 元组赋值到元组
    for book_name, author in zip(book_name, author):
        print(book_name + " : " + author)


if __name__ == "__main__":
    main()