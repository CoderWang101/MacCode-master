# fa=open('/Users/white/Desktop/Code/MacCode-master/PYproject/pythonProject/prime/file/file.txt', 'w', encoding='utf-8')
# f = open('file/file.txt', 'r+', encoding='utf-8')  # 相对路径
def read_file():
    f = open('file/file2.txt', 'a+', encoding='utf-8')  # 相对路径

    # 读出所有内容
    txt = f.read()
    f.write('Hello')
    f.write(' World')
    print(txt)
    print(txt)
    f.close()


# def read_line():
#     # 读一行
#     f = open('file/file3.txt', 'r+', encoding='utf-8')
#     while True:
#         txt = f.readline()
#         if txt:
#             break
#         print(txt)
#     f.close()
'''Python不支持重载'''


def read_line(l):
    # 读一行
    f = open('file/file3.txt', 'r+', encoding='utf-8')
    str_list = f.readline(l)#读一行
    # str_list = f.readlines(l)#返回列表
    print(str_list)
    f.close()


if __name__ == '__main__':
    read_line(10)
    read_line()
