# import my_page15
# import calu as ca

# calc = ca.Calculator(10)
# calc.divide(2)
# print(calc)
import random
from calu import Calculator as ca
import sys  # 输出包的路径

print(sys.path)

compute = ca()
compute.add(100)
print(compute)  # 实例化类__str__
print('-' * 50)

print(ca.__name__)  # Calculator
print(random.__file__)