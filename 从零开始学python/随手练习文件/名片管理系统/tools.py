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
    """显示所有名片信息功能"""

    # 如果没有任何记录提示用户
    if len(card_list) == 0:
        print("当前无任何记录，请使用新增功能来添加名片。")
        return

    print("-"*30)
    print("显示【所有保存名片】")

    # 打印表头
    for i in ["姓名", "电话", "邮箱", "地址"]:
        print(i, end="\t\t")
    print()
    print("="*80)
    
    # 遍历所有字典信息
    for dic_car in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"%(dic_car["姓名"], dic_car["电话"], dic_car["邮箱"], dic_car["地址"]))
    
    print("="*80)

def find_cards():
    """查询文件功能"""

    # 提示用户输入
    find_name = input("请输入要查找的名字：")

    # 遍历列表，寻找查找的名字。
    for i in card_list:
        if i["姓名"] == find_name:
            print("ok")
            return
    else:
        print("此列表中无%s"%(find_name))    


