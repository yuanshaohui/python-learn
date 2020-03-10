import requests
from bs4 import BeautifulSoup
import csv

# 创建类
class Video:
    def __init__(self, title, up_name, up_id, score, rank, visit):
        self.title = title
        self.up_name = up_name
        self.up_id = up_id
        self.score = score
        self.rank = rank
        self.visit = visit

    def content(self):
        return [self.title, self.up_name, self.up_id, self.score, self.rank, self.visit]

    @staticmethod
    def csv_title():
        return ["标题", "up名字", "up的id", "得分", "排名", "浏览量"]


url = "https://www.bilibili.com/ranking"
videos = []  # 创建列表

# 发送请求，获得html
response = requests.get(url)
html_text = response.text

# 解析html页面
soup = BeautifulSoup(html_text, "html.parser")
items = soup.findAll("li", {"class": "rank-item"})
for item in items:
    title = item.find("a", {"class": "title"}).text
    score = item.find("div", {"class": "pts"}).find("div").text
    rank = item.find("div", {"class": "num"}).text
    visit = item.find("span", {"class": "data-box"}).text
    up_name = item.find_all("a")[2].text
    up_id = item.find_all("a")[2].get("href")[21:]
    v = Video(title, up_name, up_id, score, rank, visit)  # 导入类
    videos.append(v)
    print(title)

# 新建csv文件
file_name = "top100.csv"
with open(file_name, "w", newline="") as f:
    pen = csv.writer(f)
    pen.writerow(Video.csv_title())
    for v in videos:
        pen.writerow(v.content())
