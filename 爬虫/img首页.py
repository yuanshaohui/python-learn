import requests
import re
import os
import time


def html_0(url_name):
    # 请求
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    response = requests.get(url_name, headers = headers)
    response.encoding = "IE=edge"
    html = response.text
    
    #分析
    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    title_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0]
    class_name = re.findall('<span itemprop="name" class="text-muted">(.*?)</span>', html)[1]
    dir_name = class_name + "-" + title_name
    
    #创建文件
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    #写入
    for url in urls:
        time.sleep(1)
        file_name = url.split("/")[-1]
        print(file_name)
        response = requests.get(url, headers = headers)
        with open(dir_name + "/" + file_name, "wb") as f:
            f.write(response.content)

url_11 = "https://www.vmgirls.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
response = requests.get(url_11, headers = headers)
response.encoding = "IE=edge"
html = response.text
urls = re.findall('<a class=".*?" href="(.*?)" title=".*?"', html)
for i in urls:
    print(i)
    html_0(i)
