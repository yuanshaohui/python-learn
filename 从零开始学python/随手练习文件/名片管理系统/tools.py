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
            for im in ["姓名", "电话", "邮箱", "地址"]:
                print(im, end="\t\t")
            print()
            print("="*80)
            print("%s\t\t%s\t\t%s\t\t%s"%(i["姓名"], i["电话"], i["邮箱"], i["地址"]))           
            print("="*80)
            del_card(i)
            break
    else:
        print("此列表中无%s"%(find_name))    

def del_card(dict_card):
    """查找到后要进行的操作"""

    #1. 提示信息，并输入
    action_str = input("请选择要执行的操作：【1】修改 【2】删除 【3】返回上级菜单")

    #2. 条件语句，判断选择
    # 修改
    if action_str == "1":
        dict_card["姓名"] = change_card("姓名", dict_card["姓名"])
        dict_card["电话"] = change_card("电话", dict_card["电话"])
        dict_card["邮箱"] = change_card("邮箱", dict_card["邮箱"])
        dict_card["地址"] = change_card("地址", dict_card["地址"])

    # 删除
    elif action_str == "2":
        card_list.remove(dict_card)
    
    # 返回上一级菜单
    else:
        return

def change_card(in_value, original):
    """在修改命令中通过回车跳过不修改的项目"""

    # 1.提示，输入
    choice = input(in_value)

    # 2.判断输入 
    if len(choice) > 0:
        return choice
    else:
        return original



