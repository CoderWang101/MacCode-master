class Father:
    def __init__(self, name="xxx", age=None, weight=None, height=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # print(s2)
    def __str__(self):  # print(s2)调用
        return f"姓名{self.name},年龄 {self.age} 体重{self.weight} 身高{self.height}"


class swimmer:
    def __init__(self, swim):
        self.swim = swim

    def __str__(self):
        return f"{self.swim}"


# class son(Father, swimmer):
#     pass
class son(Father, swimmer):
    def __init__(self, name, age, weight, height, swim):
        # 调用Father的__init__方法，传递前4个参数
        Father.__init__(self, name, age, weight, height)
        # 调用swimmer的__init__方法，传递最后一个参数
        swimmer.__init__(self, swim)

    def __str__(self):
        # 组合两个父类的字符串表示
        return f"{Father.__str__(self)}，游泳技能: {self.swim}"


if __name__ == '__main__':
    s1 = Father("张三", 50, 188, 66)
    s2 = son("李四", 18, 188, 66, "yes")
    print(s2)