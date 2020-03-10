import requests
from requests.exceptions import RequestException  # 防止requests异常
import re  # 正则分析


# 定义单页面抓取
def get_one_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:  # 判断状态码
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('.*?board-index.*?>(.*?)</i>', re.S)  # re.S是为了匹配换行符
    items = re.findall(pattern, html)
    return items

def main():
    url = "https://maoyan.com/board"
    html = get_one_page(url)
    # print(html)
    parse_one_page(html)

if __name__ == '__main__':
    main()

'''<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name'
    + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)'
    + '</i>.*?fraction">(.*?)</i>.*?</dd>
'''