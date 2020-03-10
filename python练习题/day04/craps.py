"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子。
玩家进入游戏时有1000元的赌注 全部输光游戏结束。
知识：1: if中的“==”为比较运算符，“=”代表赋值运算，恒为True。
      2: 运行程序和展示交互程序同样重要。
      3: print("1234", "5678", number)可进行字符串拼接。
      4: key = 5678   print("你好", end = "key")  end中只能为字符串。
      5：可将while的布尔值进行条件赋值，从而可以隐藏或显现该功能。
框架：输入值判断模块二-------------->第一次摇色子循环------------->第一次条件触发 + 第二次循环
拓展：可用于不同规则的多个阶段，用带布尔值的if语句，去触发隐藏的下个阶段规则。

first Author and learning from:骆昊 https://github.com/ZiniuLu/Python-100-Days/blob/master/Day01-15/Day05/craps.py
Author：袁亮亮
Date:2019-11-26
"""
from random import randint

money = 1000
while money > 0:
    print("你的总资产为：%d" % money)
    key = False
    while True:  # 对下注金额判断模块儿
        date = int(input("输入要下注的金额："))
        if 0 < date <= money:
            break
        else:
            print("输入的金额超出你拥有的")
            print("你的总资产为：%d" % money)
    first = randint(1, 6) + randint(1, 6)
    print("玩家摇出了%d点" % first)
    if first == 7 and first == 11:
        money += date
        print("玩家赢")
    elif first == 2 and first == 3 and first == 12:
        money -= date
        print("庄家赢")
    else:
        key = True
    while key:  # 循环语句是否开启，由条件语句控制。
        second = randint(1, 6) + randint(1, 6)
        print("玩家摇了%d点" % second)
        if second == 7:
            money -= date
            print("庄家赢")
            key = False
        elif second == first:
            money += date
            print("玩家赢")
            key = False

print("你破产了，游戏结束！")
