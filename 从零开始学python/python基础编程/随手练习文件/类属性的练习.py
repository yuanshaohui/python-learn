'''
@Author: your name
@Date: 2020-03-16 15:44:49
@LastEditTime: 2020-03-16 15:55:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\类属性的练习.py
'''
class Tool(object):

    # 调用的次数
    count = 0

    def __init__(self, name):

        self.name = name
        
        # 让类属性+1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")

print(Tool.count)