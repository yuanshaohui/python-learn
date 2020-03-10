"""
Author:袁亮亮
Date:2019-11-24
打印乘法口诀表
利用两个for循环来进行表格格式
"""
for i in range(1,10):      #确定大数据集的范围
    for j in range(1, i+1):    #框定小数据集的单边界限
        print("%d * %d = %d" % (i, j, i*j))


