'''
@Author: your name
@Date: 2020-03-19 11:40:42
@LastEditTime: 2020-03-19 16:35:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\爬虫\爬虫基础\练习项目\cookie_3.py
'''
from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar
from urllib.request import urlencode

# 登陆

# 保存cookie到文件中
def get_cookie():

    # 创建url
    login_url = "*****"

    # 构建伪装头
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 构建伪装用户登陆
    form_data = {
        "user": "*****"
        "pasword":"*****"
    }

    f_data = urlencode(form_data).encode()
    re = Request(login_url, headers=headers, data=f_data)  # 构建请求头


    cookie_jar = MozillaCookieJar()    # 保存cookie文件
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)  # 构建opener对象
    response = opener.open(re)  # 准备返回值

    # 保存cookie值到文件
    cookie_jar.save("cookie.txt", ignore_expires = True, ignore_discard = True)


# 从文件获取cookie
def use_cookie():
    info_url = "*****"
        # 构建伪装头
    headers = {
        "User-Agent": UserAgent().chrome
    }

    re = Request(info_url, headers=headers,)  # 构建请求头
    cookie_jar = MozillaCookieJar()    # 保存cookie文件
    cookie_jar.load("cookie.txt", ignore_expires = True, ignore_discard = True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)  # 构建opener对象
    response = opener.open(re)  # 准备返回值
    print(response.read().decode())  # 打印结果


# 主函数
def main():
    get_cookie()
    use_cookie()


# 测试函数
if __name__ == "__main__":
    main()