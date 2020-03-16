'''
@Author: 亮亮
@Date: 2020-03-16 19:34:04
@LastEditTime: 2020-03-16 19:48:37
@LastEditors: Please set LastEditors
@Description: 对类属性、类方法、静态属性、实例属性、实例方法的练习
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\game_类的综合练习.py
'''
class Game(object):

    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("帮助信息：不让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录:%d" % cls.top_score)

    def start_game(self):

        print("%s开始游戏了" % self.name)

# 1. 查看游戏的帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game = Game("小明")
game.start_game()