class Calculator:
    """简单计算器，支持连续运算和链式调用"""

    def __init__(self, initial_value=0):
        """初始化计算器，可设置起始数值，默认为0"""
        self.current = initial_value

    def add(self, num):
        """加法"""
        self.current += num
        return self

    def subtract(self, num):
        """减法"""
        self.current -= num
        return self

    def multiply(self, num):
        """乘法"""
        self.current *= num
        return self

    def divide(self, num):
        """除法，自动处理除零错误"""
        if num == 0:
            raise ValueError("除数不能为0")
        self.current /= num
        return self

    def reset(self, value=0):
        """重置当前值"""
        self.current = value
        return self

    def result(self):
        """返回当前计算结果"""
        return self.current

    def __str__(self):
        """打印当前值"""
        return str(self.current)

    def __repr__(self):
        return f"Calculator({self.current})"


# ---------- 使用示例 ----------
if __name__ == '__main__':
    calc = Calculator(10)

    # 链式调用：10 + 5 - 3 * 2 / 4
    calc.add(5).subtract(3).multiply(2).divide(4)
    print(calc)  # 输出 6.0
    print(calc.result())  # 输出 6.0

    # 重置后计算
    calc.reset(100)
    calc.divide(4).add(20)
    print(calc)  # 输出 45.0

    # 错误处理
    try:
        calc.divide(0)
    except ValueError as e:
        print("错误:", e)  # 错误: 除数不能为0