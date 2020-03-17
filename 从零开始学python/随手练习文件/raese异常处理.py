'''
@Author: your name
@Date: 2020-03-17 11:16:34
@LastEditTime: 2020-03-17 11:48:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\raese异常处理.py
'''
def pass_world():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度>8返回密码
    if len(pwd) >= 8:
        return pwd

    # 3. 判断密码长度<8抛出异常
    else:
        ex = Exception("密码长度不够")
        raise ex
try:
    print(pass_world())

except Exception as result:
    print(result)
    