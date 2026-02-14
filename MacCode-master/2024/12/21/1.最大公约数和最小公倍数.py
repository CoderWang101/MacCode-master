#最大公约数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
#最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)
    
a=gcd(12, 18)
print(a)

b=lcm(32, 24)
print(b)