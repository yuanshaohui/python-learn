import requests
import re
import time
import os


# 请求网页
# 伪装头(字典格式)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
response = requests.get("https://www.vmgirls.com/12985.html", headers = headers)
response.encoding = "IE=edge"
html = response.text


# 分析网页（正则表达式），分析网页（beautifulsoup）略
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?"', html)  # 此处要单引号，不然会报错
dir_name = re.findall('<title>(.*?)</title>', html)


# 创建文件夹
if not os.path.exists(dir_name[0]):
    os.mkdir(dir_name[0])


# 图片保存
for url in urls:
    file_name = url.split("/")[-1]
    print(file_name)
    response = requests.get(url, headers = headers)
    with open(dir_name[0] + "/" + file_name, "wb") as f:
        f.write(response.content)
        # print(file_name)
