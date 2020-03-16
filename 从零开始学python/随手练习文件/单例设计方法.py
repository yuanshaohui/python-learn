'''
@Author: your name
@Date: 2020-03-16 21:14:50
@LastEditTime: 2020-03-16 21:57:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\单例设计方法.py
'''
class Music(object):

    # 用来判断new（对象的内存调用方法）
    instance = None

    # 用来判断init（对象的初始化方法）
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否为空对象
        if cls.instance is None:
            # 2. 调用父类的方法分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象
        return cls.instance

    def __init__(self):
        
        # 1. 判断是否执行过初始化动作
        if Music.init_flag:
            return             
        
        # 2. 若没有执行则执行初始化动作
        print("执行初始化动作")

        # 3. 修改类属性的标记
        Music.init_flag = True 

play = Music()
play2 = Music()
print(play)
print(play2)