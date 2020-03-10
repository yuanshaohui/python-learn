from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

base_url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start={}&limit=20"
headers = {
    "User-Agent":UserAgent().chrome
}
i = 0
while True:
    url = base_url.format(i*20)
    request = Request(url, headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    if info == "" or info is None:
        break
    i += 1