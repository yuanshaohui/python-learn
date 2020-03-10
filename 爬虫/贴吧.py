from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()


def save_html(file_name, html_byte):  # 二进制，不用encode。
    with open(file_name, "wb") as f:
        f.write(html_byte)


def main():
    content = input("请输入贴吧名字：")
    num = int(input("请输入要下载的页数："))
    base_url = "https://tieba.baidu.com/f?&ie=utf-8&{}"
    for pn in range(num):
        args = {
            "kw": content,
            "pn": pn*50
        }
        args = urlencode(args)
        file_name = "第" + str(pn+1) + "页.html"
        print("正在保存" + file_name)
        html_byte = get_html(base_url.format(args))
        save_html(file_name, html_byte)

    pass


if __name__ == __name__:
    main()
