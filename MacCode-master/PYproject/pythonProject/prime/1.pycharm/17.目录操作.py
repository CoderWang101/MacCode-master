import os  # 文件操作模块

os.rename('file2/file3.txt', 'file2/file3.txt')
# os.remove('file2/file3.txt')
print(os.listdir())  # s输出目录文件列表
way = os.getcwd()  # 获取当前目录
print(way)
os.mkdir('file3')  # 创建文件夹
os.rmdir('file3')  # 只能删除非空文件夹

# 判断是否是文件夹
s = os.path.isabs('file3')
print(s)
print(os.path.isabs('file2'))
