"""
字典
"""


def dict_add_modify():
    dict1 = {}  # 初始化
    del dict1  # 删除字典

    student = {"张三": "2", "3": "4", "5": "6", "7": "8"}
    print(student)

    # 添加
    student['wangwu'] = 12
    print(student)
    # 修改
    student['wangwu'] = 30
    print(student)

    print(student.keys())  # 关键字
    print(student.values())  # 值
    print(student.items())
    print(student.pop("7"))

    student.setdefault("wangwu", 12)  # 不存在该元素才插入,存在不修改
    student.setdefault("python", 12)
    print(student)

    # 删除最后一个添加对键值对
    # del student['wangwu']#删除具体键值对
    # print(student)
    print(student.popitem())

    # 清除
    student.clear()
    print(student)


def dict_get():
    dict1 = {"name": "Wang", "age": 12, "height": 69.9}
    # 通过名字找元素
    print(dict1["name"])
    # 获取元素
    s = dict1.get("age")
    print(s)

    print('-' * 20)
    for key in dict1.keys():
        print(key)

    print('-' * 20)
    for val in dict1.values():
        print(val)

    print('-' * 20)
    for k, v in dict1.items():
        print(k, v)
    print('-' * 5)
    for item in dict1.items():
        print(item)
    print('-' * 20)

    new_item = dict1.items()  # 相当于迭代器
    print(type(new_item))
    print(new_item)
    dict1["name"] = "zhangsan"
    print(new_item)
    dict1.clear()


def dict_work():
    shoppe_recod = {
        "小明": {
            "fruit": ["苹果", "草莓", "香蕉"],
            "cost": 89
        },
        "小红": {
            "fruit": ["葡萄", "橘子", "樱桃"],
            "cost": 87
        }
    }

    # 统计总花费分
    total_cost = 0
    print(shoppe_recod.keys())
    print(shoppe_recod.values())
    for costs in shoppe_recod.values():
        total_cost += costs["cost"]
    print("共花费:", total_cost)

    # 统计水果种类
    dict_fruit = set()  # 集合:去重
    for category in shoppe_recod.values():
        fruit_list = category["fruit"]
        for fuit in fruit_list:
            dict_fruit.add(fuit)
    print("所有水果种类（去重）:", dict_fruit)


def my_set():
    set1 = set("wasnsasgssad")
    print(set1)  # 集合:去重
    # 集合本身无序,且无法排序
    print('a' in set1)
    set1.add(123)
    print(set1)
    a = [1, 2, 3, 4, 5]
    b = a.copy()
    print(id(a))
    print(id(b))
    c = 1
    d = c
    # c+=1
    print(id(c))
    print(id(d))
    print(d)


# dict_add_modify()
# dict_get()
# dict_work()
# 集合
my_set()
