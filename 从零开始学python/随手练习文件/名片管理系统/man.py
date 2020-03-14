import tools

while True:

    # 显示模块儿
    tools.show_mnu()
    
    chose = input("请选择要操作功能：")
    print("您选择的功能是【%s】"%(chose))
    if chose in ["1", "2", "3"]:

        # 新增名片
        if chose == "1":
            tools.new_cards()
            
        # 显示全部名片
        elif chose == "2":
            tools.all_cards()
            

        # 查询名片
        elif chose == "3":
            tools.find_cards()

    # 退出系统    
    elif chose == "0":
        print("欢迎下次使用！")
        break
    
    else:
        print("请输入正确的格式。")