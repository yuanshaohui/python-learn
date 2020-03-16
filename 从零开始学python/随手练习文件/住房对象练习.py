'''
@Author: 亮亮
@Date: 2020-03-16 10:25:18
@LastEditTime: 2020-03-16 11:37:00
@LastEditors: Please set LastEditors
@Description: 住房家具搭配
@FilePath: \giee\learn_python\从零开始学python\随手练习文件\住房对象练习.py
'''
class HouseItem:
    """创建家具类"""

    def __init__(self, name, area):
        
        self.name = name
        self.area = area

    def __str__(self):

        return "【%s】占地 %.2f" % (self.name, self.area)

class House:
    """创建房子"""

    def __init__(self, house_type, area):
        
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n总面积：%.2f【剩余：%.2f】\n家具：%s" 
                % (self.house_type, self.area, self.free_area, self.item_list))
    
    def add_item(self, item):

        print("要添加%s" % item)

        # 1.对家具的面积进行判断
        if item.area > self.free_area:
            print("%s的面积太大，无法添加" % item.name)

            return

        # 2. 将家具名添加到列表中去
        self.item_list.append(item.name)

        # 3. 计算剩余的面积
        self.free_area -= item.area


# 创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 20)

# 创建房子对象
house = House("两室一厅", 60)
house.add_item(bed)
house.add_item(bed)
house.add_item(chest )

print(house)


