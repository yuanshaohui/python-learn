"""
输出2~99之间的素数
知识点：1. 新定义的局部变量只在局部有效。
        2.每一次for循环key值会重新定义。
        3.对于for循环为主干的程序，可根据应用场景进行缩减搜索范围来进行优化。

first Author and learning from:骆昊 https://github.com/ZiniuLu/Python-100-Days/blob/master/Day01-15/Day05/prime.py
Version:0.1
Author：袁亮亮
Date:2019-11-26
"""
for i in range(2, 100):
    key = True
    for j in range(2, i):
        if i % j == 0:
            key = False
    if key:
        print(i, end = " ")

# import math
#
# for num in range(2, 100):
# 	is_prime = True
# 	for factor in range(2, int(math.sqrt(num)) + 1):    #用开方的形式减少搜索范围，优化运算
# 		if num % factor == 0:
# 			is_prime = False
# 			break
# 	if is_prime:
# 		print(num, end=' ')
