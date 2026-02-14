class Person:
    # 类属性
    count = 0

    def __init__(self, name="xxx", age=None):
        self.name = name
        self.age = age
        Person.count += 1

    # print(s2)
    def __str__(self):  # print(s2)调用
        return f"姓名{self.name},年龄 {self.age}"


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # 放置多继承重复调用(super只调用一次)


s1 = Student("张三", 30)
s2 = Student("l", 20)
s3 = Student("x", 10)
print(s1.count)
