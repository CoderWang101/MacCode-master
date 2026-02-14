# 一切皆引用
a = 10
b = 10
print("a_id=", id(a))
print("b_id=", id(b))
'''
4336398544
4336398544
a,b地址相同
'''
print('-' * 50)


def c_id():
    c = 10
    print("c_id=", id(c))


c_id()
d = 10
print("d_id=", id(d))
'''
4377800912
4377800912
c,d地址相同
'''
print('-' * 50)


def change(num):
    num = 10
    print(f"函数中的num{num}")


num = 20
print(f"初始的num{num}")
change(num)
print(f"执行函数后的num{num}")
print('-' * 50)


def change_list(num):
    num = [5, 6, 7]
    print(f"函数中的list{num}")


my_list = [1, 2, 3]
print(f"初始的my_list{my_list}")
change_list(my_list)
print(f"执行函数后的my_list{my_list}")

print('-' * 50)
print("只能更改可变参数\n个更改列表的具体值")
print(f"my_list{my_list},my_list_id={id(my_list)}")


def change_list2(my_list):
    my_list[0] = 10


change_list2(my_list)
print(f"更改后的my_list{my_list},my_list_id={id(my_list)}")  # 地址相同
