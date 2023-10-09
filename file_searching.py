# 文件查找工具
# 输入查找路径，输入要搜索的文件名
# 自动在指定路径下查找

# 递归查找，遇到子目录，进入目录里进行查找
# 使用标准库关键函数 os.walk 只需要使用简单循环就可以完成递归遍历，不用手写
import os

inputPath = input('请输入要搜索的路径：')
pattern = input('请输入要搜索的关键词：')

for dirpath, dirnames, filenames in os.walk(inputPath):

 # 遍历到当前位置对应的路径；当前目录下有哪些目录，是一个列表可包含多个目录名；当前目录下都有哪些文件名，是一个列表可包含多个文件名
# os.walk 每次调用，都能自动地去针对子目录进行递归操作，只需要使用上述循环，就可以把所有的路径都获取出来
#     print('--------------------------------------------------')
#     print(f'dirpath = {dirpath}')
#     print(f'dirnames = {dirnames}')
#     for name in dirnames:
#         print(name)
#     print('filemanes:')
#     for name in filenames:
#             print(name)

    for f in filenames:
        if pattern in f:
            print(f'{dirpath}\{f}')
