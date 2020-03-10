from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


url = "???"
form_data = {
    "user": "17853680108"
    "passworld":"asdfsd"
}
headers = {
    "User-Agent": UserAgent().chrome
}
f_data = urlencode(form_data)
request = Request(url, data=f_data.encode(), headers=headers)
response = urlopen(request)
