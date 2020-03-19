'''

'''

from urllib.request import urlopen, Request
from fake_useragent import UserAgent

def main():
    # 发送请求
    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=4000&limit=20"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    try:
        request = Request(url, headers=headers)
        response = urlopen(request)

        # 读取内容
        info = response.read()

        # 打印内容
        print(info.decode())
    
    except URLError as e:
        print(e)
    
    print("访问完成")


if __name__ == "__main__":
    main()