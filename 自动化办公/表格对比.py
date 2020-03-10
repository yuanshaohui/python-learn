import xlrd

# G:\机制本二花名册.xlsx
# G:\机制本二花名册2.xls
# 输入模块儿
# 文件地址
data_address = str(input("输入模板文件地址："))
data_address2 = str(input("输入对比文件地址："))
date_sheet = int(input("输入要对比的第几个共同表单：")) - 1


# 文件格式转换函数
def data_format(data):
    data_1 = data.encode(encoding="utf-8")
    data_2 = data_1.decode(encoding="utf-8")
    return data_2


# 打开文件表单函数
def open_name(data, sheet_number):
    open_excel = xlrd.open_workbook(data)
    open_sheet = open_excel.sheet_by_index(sheet_number)
    return open_sheet


# 主体
data_address = data_format(data_address)
data_address2 = data_format(data_address2)
sheet_1 = open_name(data_address, date_sheet)
sheet_2 = open_name(data_address2, date_sheet)

# 遍历每个表格
nrow = []
ncol = []
data_1 = []
data_2 = []
k = 0
for i in range(0, sheet_1.nrows):
    for j in range(0, sheet_1.ncols):
        table_1 = sheet_1.cell_value(i, j)
        table_2 = sheet_2.cell_value(i, j)
        if table_1 != table_2:
            k += 1
            nrow.append(i)
            ncol.append(j)
            data_1.append(table_1)
            data_2.append(table_2)
            continue
print("总共有{}个不同之处".format(k))
for i in range(len(nrow)):
    print("第{}处， 第{}行， 第{}列, 模板表格内容：{}, 对比表格内容：{} "
          "".format(i + 1, nrow[i], ncol[i], data_1[i], data_2[i]))
