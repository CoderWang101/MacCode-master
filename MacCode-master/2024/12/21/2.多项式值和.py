def cal_multi_items(n, A, x):
    """
    n (int): 多项式的项数，即系数列表A的长度。
    A (list): 多项式的系数列表，A[0]是常数项，A[n-1]是最高次项的系数。
    x (float): 自变量x的值。
    返回:
    temp (float): 多项式在x处的值。
    """
    # 初始化temp为最高次项的系数
    temp = A[n-1]
    
    # 从最高次项开始，逐项计算多项式的值
    for i in range(n-1, 0, -1):
        temp = temp * x + A[i-1]# 每次迭代，将当前的temp乘以x，再加上下一项的系数
    return temp

cal = cal_multi_items(4, [1, 2, 3, 4], 1)
print(cal)  # 输出结果