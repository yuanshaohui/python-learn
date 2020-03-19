'''
@Author: your name
@Date: 2020-03-19 20:28:16
@LastEditTime: 2020-03-19 20:42:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request库_5cookie的使用.py
'''
import requests 
from fake_useragent import UserAgent

def main():

    # 构建session
    session = requests.Session()

    # 构建url
    login_url = "*****"

    # 构建用户名密码param
    form_data ={
        "user": "****",
        "passworld": "*****"
    }

    # 构建伪装头
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 接收返回对象
    response = session.get(login_url, headers=headers, params=form_data)

    # 构建登陆进去的url
    info_url = "*******"
    response = session.get(info_url, headers=headers, params=form_data)




if __name__ == "__main__":
    main()