'''
@Descripttion: 
@version: 
@Author: 亮亮
@Date: 2020-03-12 19:58:37
@LastEditors: 亮亮
@LastEditTime: 2020-03-14 22:21:08
'''
def news(num):
    print(num)
    if num == 1:
        return
    news(num - 1)
news(10)    
