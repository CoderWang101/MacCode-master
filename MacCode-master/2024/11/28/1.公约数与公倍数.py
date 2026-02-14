def gcd(a, b):
    """递归计算最大公约数"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    """递归计算最小公倍数"""
    if a == 0 or b == 0:
        return 0
    else:
        return a * b // gcd(a, b)

# 测试数据
num1 = 10
num2 = 7

# 计算最大公约数
result_gcd = gcd(num1, num2)
print(f"最大公约数: {result_gcd}")

# 计算最小公倍数
result_lcm = lcm(num1, num2)
print(f"最小公倍数: {result_lcm}")