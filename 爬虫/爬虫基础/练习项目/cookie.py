'''
@Author: your name
@Date: 2020-03-19 10:10:43
@LastEditTime: 2020-03-19 11:44:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\cookie.py
'''
from urllib.request import Request, urlopen
from fake_useragent import UserAgent


url = ""
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": ''
}
request = Request(url, headers=headers) 
response = urlopen(request)
print(response.read().decode())