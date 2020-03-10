"""
多种简单几何体的运算
Author: 袁亮亮
Date: 2019 - 11 - 20
"""
import math

a = int(input("1.圆形 2.矩形 3.梯形 4.三角形  您选择计算的图形编号为："))
if a == 1:
    r = float(input("半径= "))
    s = math.pi * r ** 2
    l = 2 * math.pi * r
    print("面积=%.01f平方米,周长=%.01f米" % (s, l))
elif a == 2:
    long = float(input("其中一边="))
    long2 = float(input("另一边="))
    s = long * long2
    l = 2 * (long + long2)
    print("面积=%.01f平方米，周长=%.01f米" % (s, l))
elif a == 3:
    up = float(input("上底="))
    down = float(input("下底="))
    h = float(input("高="))
    s = ((up + down) * h) / 2
    print("面积=%.01f平方米" % s)
elif a == 4:
    down = float(input("底="))
    h = float(input("高="))
    s = (down * h) / 2
    print("面积=%.01f平方米" % s)
