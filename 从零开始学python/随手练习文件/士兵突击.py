'''
@Author: your name
@Date: 2020-03-16 11:38:32
@LastEditTime: 2020-03-16 13:34:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\士兵突击.py
'''
class Gun:
    
    def __init__(self, model):

        # 1. 枪的型号
        self.model = model

        # 2. 剩余子弹数量
        self.bulled_count = 0

    def add_bulled(self, count):

        self.bulled_count += count
    
    def shoot(self):

        # 1. 判断子弹数量
        if self.bulled_count <= 0:

            print("子弹已经用光，请装填子弹")
            return

        # 2. 发射子弹
        self.bulled_count -= 1

        # 3. 提示发射信息
        print("【%s】突突突.....【%d】" % (self.model, self.bulled_count))

class Soldier:

    def __init__(self, name):

        # 1. 姓名
        self.name = name

        # 2. 枪 -新兵没有枪
        self.gun = None

    def fire(self):

        # 1. 判断是否有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)

            return
        
        # 2. 高喊口号
        print("冲呀.....%s" % self.name)

        # 3. 让枪装上子弹
        self.gun.add_bulled(50)

        # 4. 让枪发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo)