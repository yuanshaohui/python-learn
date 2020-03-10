"""
模拟网站用户登陆
Author:袁亮亮
Date:2019-11-19
"""


name = "袁亮亮"
pass_word = "123456"
c = 0
for i in range(3):
    a = input("please input your name:")
    b = input("please input your password:")
    c = c + 1
    if a == name:
        if b == pass_word:
            print("welcome {}".format(a))
            break
        else:
            print("please resume load your password")
    elif c == 3:
        print("your account is locked")
    else:
        print("lease resume load your name")
