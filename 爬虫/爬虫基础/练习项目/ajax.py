'''
@Author: your name
@Date: 2020-03-18 22:40:00
@LastEditTime: 2020-03-18 23:14:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\ajax.py
'''
from urllib.request import Request, urlopen
from fake_useragent import UserAgent


def html_one(num):
    # 构建url
    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=1".format(num)

    # 构建伪装头
    ua = UserAgent()
    headers = {
        "User-Agent" : ua.chrome
    }

    # 构建Request
    request = Request(url, headers=headers)

    # 构建返回
    response = urlopen(request)

    # 读取返回值
    recv_data = response.read().decode()
    
    return recv_data



def main():

    # 循环页数
    num = 0
    while True:
        data = html_one(num)
        
        # 判断退出
        if not data or data == "":
            break
        print(data)
        print("---------第{}页-------".format(num/20))
        num += 20

    print("爬取结束")


if __name__ == "__main__":
    main()