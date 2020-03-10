"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
知识点：1： 将一组数分割开可用“%”或“//”


first Author and learning from:骆昊 first Author and learning from:骆昊 https://github.com/ZiniuLu/Python-100-Days/blob/master/Day01-15/Day05/craps.py
Author：袁亮亮
Date:2019-11-27
"""
for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    answer = high ** 3 + mid ** 3 + low ** 3
    if answer == i:
        print(i)
#sdfs