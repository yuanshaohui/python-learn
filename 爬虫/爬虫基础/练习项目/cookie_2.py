'''
@Author: 亮亮
@Date: 2020-03-19 10:26:01
@LastEditTime: 2020-03-19 10:42:13
@LastEditors: Please set LastEditors
@Description: 模拟登陆
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\cookie_2.py
'''
from urllib.request import Request, urlopen, HTTPCookieProcessor
from fake_useragent import UserAgent
from urllib.parse import urlencode

# 登陆
login_url = ""
headers = {
    "User-Agent": UserAgent().chrome,
}
form_data = {
    "user":"",
    "password":""
}
request = Request(login_url, headers=headers, data=form_data)
# response = urlopen(request) #  构建opener
handler = HTTPCookieProcessor
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())



# 访问页面
url = "https://www.zhihu.com/explore"
request = Request(url, headers=headers) 
# response = urlopen(request)
response = opener.open(request)
print(response.read().decode())