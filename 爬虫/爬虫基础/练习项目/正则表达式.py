'''
@Author: your name
@Date: 2020-03-19 21:24:32
@LastEditTime: 2020-03-19 21:36:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\正则表达式.py
'''
import re

strl = "I study python3.7 Everday"
print("---------match()---------")  # match从头开始匹配
m1 = re.match(r"I", strl)
m2 = re.match(r"\w", strl)
m3 = re.match(r".", strl)
m4 = re.match(r"\D", strl)
print(m4.group())