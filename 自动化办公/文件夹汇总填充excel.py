from xlutils.copy import copy
import xlrd
import xlwt
import os

#输入模块
file_dir = str(input("请输入文件夹地址："))
name = str(input("请输入生成文件名："))
address = str(input("请输入模板文件名："))
data_sheet = int(input("请输入要合并第几个表单"))-1


#文件格式转换函数
def data_format(data):
    data_1 = data.encode(encoding = "utf-8")
    data_2 = data_1.decode(encoding = "utf-8")
    return data_2

#字典合并函数
def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

#文件夹操作函数
def folder(file_dir):
    data = os.listdir(file_dir)
    return data

#文件表单操作函数
def open_sheet(data):
    open_sheet1 = xlrd.open_workbook(data)
    open_sheet2 = open_sheet1.sheet_by_index(0)
    return open_sheet2

#文件地址合成函数
def address_file(name1, name2):
    name = name1 + "/" + name2
    return name

#单文件操作函数
def excel(name_1):
    sheet = open_sheet(name_1)
    dict_1 = {}
    for x in range(0, sheet.nrows):
        for y in range(0, sheet.ncols):
            table_1 = sheet.cell_value(x, y)
            if table_1 != "":
                dict_1[(x, y)] = table_1
                continue
    return dict_1

#新建文档函数
def new_workbook():
    # 初始化样式
    # 创建一个新模板
    style = xlwt.XFStyle()

    # 创建字体
    font = xlwt.Font()
    # 字体
    font.name = "微软雅黑"
    # 加粗
    font.bold = True
    # 字号*20
    font.height = 200
    style.font = font

    # 边框
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    style.borders = borders

    # 对齐
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment

    return style


#操作
dict = {}
for i in folder(file_dir):
    dict_1 = excel(address_file(file_dir, i))
    dict = merge(dict_1, dict)
open_excel = xlrd.open_workbook(address_file(file_dir, address + ".xlsx"))
new_excel = copy(open_excel)
new_sheet = new_excel.get_sheet(0)
new_workbook()
for i in dict.keys():
    new_sheet.write(i[0], i[1], dict[i], new_workbook())
new_excel.save(address_file(file_dir, name + ".xls"))

