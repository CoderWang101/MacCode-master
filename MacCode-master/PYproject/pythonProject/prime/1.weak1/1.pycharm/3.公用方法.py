def compare_():
    list_a = [1, 2, 3, 4]
    list_b = [2, 3, 4, 5]
    print(list_a > list_b)  # False

    list_c = "hello"
    list_d = "world"
    print(list_c > list_d)


def function_():
    list1 = 'asdhfjlka'
    mylist = list(list1)
    print(mylist)
    sorted(mylist)
    print(mylist)

    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(sorted(dict1, reverse=True))

    # 枚举
    print('-' * 50)
    for pos, value in enumerate(mylist):  # 把每个元素的位置取出来
        print(pos, value)


# compare_()
function_()
