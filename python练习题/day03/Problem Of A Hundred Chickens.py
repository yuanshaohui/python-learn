"""
Author:袁亮亮
Date:2019-11-25
百钱百鸡问题，一只公鸡5元，一只母鸡3元，三只小鸡1元.一百元一百只鸡
问：多少公鸡？多少母鸡？多少小鸡？
框架：利用穷举法举出所有可能，再用条件语句来跳出符合要求的答案。
拓展：可用于n个未知数，n-1个方程，和给定未知数范围的问题。
"""
for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        money = i * 5 + j *3 + k / 3
        if money == 100:
            print("有公鸡%d只，母鸡%d只，小鸡%d只" % (i, j, k))