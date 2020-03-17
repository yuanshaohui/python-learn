'''
@Author: your name
@Date: 2020-03-17 10:29:15
@LastEditTime: 2020-03-17 10:36:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\异常处理演示.py
'''
try:
    num = int(input("请输入除数："))

    result = 8 / num
    print(result)
except ValueError:
    print("请输入合适的数值")
except ZeroDivisionError:
    print("分母不能为零")