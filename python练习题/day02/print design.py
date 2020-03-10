"""
Author:袁亮亮
Date:2019-11-24
算法：用循环语句迭代打印
学习：print()可用来空格，"_"可代表循环标志
"""
number = int(input("输入打印三角形行数："))
for i in range(number):  # 确定行数
    for j in range(i + 1):  # 确定每行个数
        print("*", end=" ")
    print()  # 可用于换行

for i in range(number):  # 代表行数迭代
    for j in range(number):  # 代表个数迭代
        if j < number - 1 - i:  # 随着行数变化空格和星星比例也在变化
            print(" ", end="")
        else:
            print("*", end="")
    print()

for i in range(number):  # 代表行数迭代
    for _ in range(number - i):  # 只看一半，空格迭代
        print(" ", end="")
    for _ in range(i * 2 + 1):  # *号迭代
        print("*", end="")
    print()
