'''
@Author: your name
@Date: 2020-03-21 10:15:33
@LastEditTime: 2020-03-21 10:35:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\爬虫--BeautifulSoup.py
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup("html", "lxml")
print("------find_all------")
print(soup.find_all("title"))
print(soup.find_all(id= "title"))
print(soup.find_all(class_= "info"))  # class 是关键字，要加下划线
print(soup.find_all("div", attrs= {"float":"left"}))  # 可传入字典