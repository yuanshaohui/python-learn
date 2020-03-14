# 名片数据库
card_list = []

def show_mnu():
    """显示模块儿"""

    print("*"*30)
    print("欢迎使用【名片管理系统】 v1.0")
    print()
    print("1. 新建文件")
    print("2. 显示全部")
    print("3. 查询名片")
    print()
    print("0. 退出系统")
    print("*"*30)
    return

def new_cards():
    """新增文件功能"""

    # 输入名片信息
    name = input("姓名：")
    phone = input("电话 ：")
    email = input("邮箱：")
    address = input("地址:")

    # 存入字典
    car_dict = {
        "姓名":name,
        "电话":phone,
        "邮箱":email,
        "地址":address
    }

    # 存入列表
    card_list.append(car_dict)
    print(card_list)
    print("保存成功！")
    return

def all_cards():
    """显示所有文件功能"""

def find_cards():
    """查询文件功能"""
