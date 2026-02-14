import random
import math

def integrand(x):
    return x * math.exp(-x**2)

def monte_carlo_integration(a, b, N):
    total = 0
    for _ in range(N):
        # 在区间 [a, b] 内随机取一个点
        x = random.uniform(a, b)
        # 计算被积函数在该点的值并累加
        total += integrand(x)
    # 计算平均值并乘以区间长度
    average = total / N
    integral = average * (b - a)
    return integral

# 定积分的上下限和迭代次数
a = 1
b = 2
N = 10000

# 计算定积分
result = monte_carlo_integration(a, b, N)
print(f"定积分 ∫_1^2 x*e^(-x^2) dx 的近似值为: {result}")