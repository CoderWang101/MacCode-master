def sum_total(*args):
    total = 0
    for i in args:
        total += i
    print(total)


def print_user(**kwargs):
    print("接收关键字参数:", kwargs)
    # print(f"姓名:{kwargs['name']},年龄:{kwargs['age']}")
    print(f"姓名:{kwargs.get('name')},年龄:{kwargs['age']}")


def print_(sum, *args, **kwargs):
    print("sum=", sum)
    print("args=", args)
    print("kwargs=", kwargs)


# sum_total(1, 2, 3, 4, 5)
# sum_total(1, 2, 3, 4, 5)
# print_user(name='bobo', age='18')
# print_user(name='bobo', age='18',gender='male')
print_(1, 2, 3, 4, 5, name="wang", age=20, gender="male")
