def horner_rule(coefficients, x):
    """计算多项式 a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0 的值
    
    参数:
    coefficients: 多项式的系数列表，从低次到高次，即 [a_0, a_1, ..., a_n]
    x: 变量 x 的值
    
    返回:
    多项式的值
    """
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result

# 测试数据
coefficients = [1, 2, 3, 4]  # 多项式: 4x^3 + 3x^2 + 2x + 1
x = 2

# 计算多项式的值
result = horner_rule(coefficients, x)
print(f"多项式的值: {result}")