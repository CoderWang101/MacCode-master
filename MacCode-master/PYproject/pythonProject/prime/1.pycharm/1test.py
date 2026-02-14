import random

number = "0123456789"
# 字符串［起始位置：结束位置：步长］
print(number[0:3])
print(number[2::2])
print(number[::3])
print(number[-3::-1])

# 1基本操作
mylist = ['小李', '小明', '嘉豪', '小张', '嘉豪', '老王', '老李', '楚云飞', '嘉豪']
print(mylist.index('小明'))  # 1
print(mylist.index('嘉豪', 3))  # 从第三个位置开始找
print(mylist.index('嘉豪', 3, 100))  # 从第三个位置开始找,第100位置结束(不足自动结束)

print('\n')

# 统计指定元素个数
print(mylist.count('嘉豪'))  # 3次
print('\n')
# in 指定元素个数是否在列表中
print('小李' in mylist)  # True
print('李' not in mylist)  # True
print('\n')

# 2.删除
mylist_2 = ['小李', '小明', '嘉豪', '小张', '嘉豪', '老王', '老李', '楚云飞', '嘉豪', '楚云飞']
print(mylist_2)
del mylist_2[3]  # 要可变的才可删除
print(mylist_2)
del mylist_2[3:5]  # 范围删除
print(mylist_2)

# 删除最后一个元素
mylist_2.pop()  # 删除最后一个元素
print(mylist_2)
mylist_2.pop(2)  # 删除指定元素

mylist_2.remove('楚云飞')  # 删除第一个匹配项目
# mylist_2.clear()  # 清空
print(mylist_2)
mylist_2 += ['嘉豪']
print(mylist_2)

list_len = len(mylist_2)
print(list_len)
print('/n')

# 列表反转
mylist_2.reverse()
print(mylist_2)

mylist_2.sort()  # 从小到大
print(mylist_2)
mylist_2.sort(reverse=True)  # 从大到小
print(mylist_2)

a, b = 1, 2
# 交换ab
a, b = b, a
print(a, b)

classroom = [[] for i in range(5)]
print(classroom)  # [[], [], [], [], []]
lecturer = [[chr(ord('A') + i)] for i in range(10)]
print(lecturer)
for teacher in lecturer:
    classroom[random.randint(0, 2)].append(teacher)
print(classroom)

'''
元祖
    定义Tuple（元组）与列表类似，不同之处在于元组内的元素不能修改。
        • 元组表示多个元素组成的序列工
        • 用于存储一串信息，数据之间使用，分隔
        •元组用（）定义
        •元组的索引从e开始
'''

'''
字典
'''
dict1 = {}  # 初始化
