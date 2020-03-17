'''
@Author: your name
@Date: 2020-03-16 20:19:47
@LastEditTime: 2020-03-16 20:35:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\__new__方法.py
'''
class Music(object):
    def __new__(cls, *args, **kwargs):

        # 1. 创建对象，new方法会自动调用
        print("创建对象，分配空间")

        # 2. 为对象创建空间
        instance = super().__new__(cls)
        
        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")

player = Music()
print(player)