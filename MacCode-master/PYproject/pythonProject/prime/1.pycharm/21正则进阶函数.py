# 实现一个和range类似的生成器
def my_range(n):
    i = 0
    while i < n:
        '''yield先拿到返回值,并再次执行到yield时冻结'''
        yield i  # 冻结当前执行位置,并返回i
        i += 1
        print("当前i:", i)
        print('*' * 10)
    return None


if __name__ == '__main__':
    g = my_range(10)  # i只能遍历一次
    print(g)
    result = next(g)
    print(result)
    result = next(g)
    print(result)
    print('-' * 50)

    for j in g:  # 2 3 ...
        print(j)

    g2 = my_range(10)  # 想再次遍历,要重新定义
