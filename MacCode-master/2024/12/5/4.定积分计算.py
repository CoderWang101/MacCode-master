import random
import math

def integrand(x):
    return x * math.exp(-x**2)

def monte_carlo_integration(a, b, n):
    sum_fx = 0.0
    for _ in range(n):
        x = random.uniform(a, b)
        sum_fx += integrand(x)
    integral = (b - a) * sum_fx / n
    return integral

# 定积分的上下限
a = 1.0
b = 2.0

# 迭代次数
n = 10000

# 计算定积分
integral_value = monte_carlo_integration(a, b, n)
print(f"定积分的值为: {integral_value}")