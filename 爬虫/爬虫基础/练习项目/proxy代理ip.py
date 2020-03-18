'''
@Author: your name
@Date: 2020-03-18 23:49:08
@LastEditTime: 2020-03-18 23:58:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\proxy代理ip.py
'''

from urllib.request import ProxyHandler
from urllib.request import build_opener

proxy = ProxyHandler({"http":"60.190.23.50"})
opener = build_opener(proxy)
url = "https://cn.bing.com/"
response = opener.open(url)
print(response.read().decode("utf-8"))