from collections.abc import Iterator, Iterable


def use_for():
    my_list = [1, 2, 3]
    print(isinstance(my_list, Iterable))  # 判断是否是可迭代对象
    list_iterator = iter(my_list)
    print(isinstance(list_iterator, Iterator))  # 判断是否是迭代器对象

    for i in list_iterator:
        print(i)  # 输出1 2 3
    # 迭代器只能遍历一次
    for i in list_iterator:
        print(i)  # 无输出

    # 重新创建一个迭代器
    list_iterator = iter(my_list)
    for i in list_iterator:
        print(i)  # 输出1 2 3


if __name__ == "__main__":
    use_for()
