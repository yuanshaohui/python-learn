'''
@Author: your name
@Date: 2020-03-18 20:28:17
@LastEditTime: 2020-03-18 20:39:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\request.py
'''
from urllib.request import urlopen

def main():
    # 发送请求
    url = "https://www.baidu.com/"
    response = urlopen(url)

    # 读取内容
    info = response.read()

    # 打印内容
    print(info.decode("utf-8"))


if __name__ == "__main__":
    main()