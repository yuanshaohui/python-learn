'''
@Author: your name
@Date: 2020-03-21 10:39:19
@LastEditTime: 2020-03-21 10:54:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\爬虫--css选择器.py
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup("html", "lxml")

print("--------CSS选择器--------")
print(soup.select("title"))  # 标签选择器
print(soup.select("#title"))  # ip选择器
print(soup.select(".info"))  # class类选择器
print(soup.select("div > span"))  # div里的span
print(soup.select("div")[1].select("span"))  # div里的span
print(soup.select("title")[0].text)  # 标签内的内容