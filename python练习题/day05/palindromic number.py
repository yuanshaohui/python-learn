"""
判断该范围内的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
知识点：1. 利用字符串切片来操作字符串



first Author and learning from:骆昊 https://github.com/ZiniuLu/Python-100-Days/blob/master/Day01-15/Day05/palindrome.py
Version:1.1
Author：袁亮亮
Date:2019-11-26
"""
begin = int(input("开始数字："))
finish = int(input("结束数字："))
for i in range(begin, finish + 1):
    number = str(i)
    number02 = number[::-1]
    if number == number02:
        print("%s 是回文数" % number)
