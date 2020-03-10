"""
关于循环语句的练习
Author:袁亮亮
Date:2019-11-23
"""
# for in 循环，range中数值为左闭区间，右开区间。可进行内容搜索遍历。
# i = 0
# for i in range(1, 100, 2):   #步距为二，从1到99的奇数
#     print(i)



"""
从一加到一百
"""
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)




"""
while函数，无限循环，由布尔值判断跳出。while提供密闭循环空间，内部提供跳出条件，可进行端口状态监控。
根据提示猜测一百以内随机数字
"""
# import random  # 随机数
#
# answer = random.randint(1, 100)
# i = 0
# while True:
#     number = float(input("请输入您猜的数字："))
#     i += 1
#     if answer > number:
#         print("小了")
#     elif answer < number:
#         print("大了")
#     else:
#         print("恭喜过关")
#         break
# print("总共用了%d次" % i)




"""
while 函数进行电脑根据我的提示猜数字,多重赋值后中间变量值还保留，循环中改变的是全局变量
"""
# answer = int(input("请输入一千以内的整数："))
# number = 0
# big = 1000
# smile = 0
# while True:
#     guss = (big + smile) / 2
#     number += 1
#     print("是不是%d" % guss)
#     my_answer = input("大了按w,小了按s，正确按y:")
#     if my_answer == "y":
#         print("总共猜了%d次" % number)
#         break
#     elif my_answer == "w":
#         big = guss
#     elif my_answer == "s":
#         smile = guss
