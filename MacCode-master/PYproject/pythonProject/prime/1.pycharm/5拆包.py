my_tuple = (1, 2)
a, b = my_tuple  # 变量个数要相等
print("a=", a, "b=", b)
print('-' * 50)


def sum_subtract(a, b):
    return a + b, abs(a - b)


a, b = sum_subtract(a, b)
print("a=", a, "b=", b)
print('-' * 50)
a, b = b, a
print("a=", a, "b=", b)
