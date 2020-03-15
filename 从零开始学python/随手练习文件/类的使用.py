'''
@Author: 亮亮
@Date: 2020-03-15 21:30:52
@LastEditTime: 2020-03-16 00:21:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\类的使用.py
'''
class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s去了" % self.name)

    def __str__(self):

        return "我是小猫【%s】" % self.name

tom = Cat("tom")
print(tom)
print("-"*50)