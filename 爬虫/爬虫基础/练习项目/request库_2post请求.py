'''
@Author: your name
@Date: 2020-03-19 20:07:11
@LastEditTime: 2020-03-19 20:10:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request_2.py
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
    data = {
        "user": "****"
        "password": "*****"
    }

    # 构建request对象
    response = requests.pose(url,headers=headers, data=data)
    print(response.text)



if __name__ == "__main__":
    main()  