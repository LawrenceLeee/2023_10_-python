# # 操作excel
#
# import xlrd.xlsx
# from xlrd import xlsx
#
# # 1.先打开xlsx文件
# xlrd.open_workbook('C:/Users\Lawrence Lee\Desktop/test.xlsx')
#
# # 2.获取到指定的标签页
# xlsx.sheet_by_index(0)
#
# # 3.获取到表格有多少行
# nrows = table.nrows
#
# # 4.进行循环统计操作
# total = 0
# count = 0
# for i in range(1, nrows):
#     # 拿到当前同学的班级id
#     class_id = table.cell_value(i, 1)
#     if class_id == 100:
#         total += table.cell_value(i, 2)
#         count += 1
# print(f'平均分：{total / count}')

g = 825
if g // 5 == 0:
    print(f'{g} is divisible by 5. ', end='\n')
if g // 11 == 0:
    print(f'{g} is divisible by 11. ', end='\n')
if g // 15 == 0:
    print(f'{g} is divisible by 15. ', end='\n')
