"""
Author:袁亮亮
Date:2019-11-24
利用for循环来找出两个正整数数的最大公约数和最小公倍数
算法：公约数整除，余数为零
      公倍数暂时没想好，以后补上
"""
x = int(input("x ="))
y = int(input("y ="))
if x < y:
    (x, y) = (y, x)    #将x设置为最大数，y设置为最小数
for i in range(x, 1, -1):
    if x % i == 0 and y % i == 0:
        print("%d 和 %d 的最大公约数为%d" % (x, y, i))
        break