"""
斐波那契数列
框架：利用（a, b）=(b, a+b)
拓展：类似函数爬行，前后关联数列



first Author and learning from:骆昊 https://github.com/ZiniuLu/Python-100-Days/blob/master/Day01-15/Day05/craps.py
Author：袁亮亮
Date:2019-11-26
"""
a = 0
b = 1
i = int(input("选择循环次数："))
for _ in range(i):
    (a, b) = (b, a+b)
    print(a, end = " ")