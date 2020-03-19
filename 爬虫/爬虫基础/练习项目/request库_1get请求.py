'''
@Author: your name
@Date: 2020-03-19 17:57:03
@LastEditTime: 2020-03-19 18:16:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request库.py
'''
import requests 
from fake_useragent import UserAgent


def main():


    # 构建url
    url = "https://www.baidu.com/"

    # 构建请求头
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 构建url扩展内容
    params = {
        "wd": "计算机   "
    }

    # 构建request对象
    response = requests.get(url,headers=headers, params=params)
    print(response.text)



if __name__ == "__main__":
    main()    