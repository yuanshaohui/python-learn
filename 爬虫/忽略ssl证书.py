from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import ssl


url = "https://www.12306.cn"
headers = {
    "User-Agent":UserAgent().chrome
}
request = Request(url, headers = headers)
# 忽略ssl证书
context = ssl._create_default_https_context()
response = urlopen(request)
print(response.read().decode())