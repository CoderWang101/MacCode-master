class Person:
    def __init__(self, name="xxx", age=None, ):
        self.name = name
        self.age = age

    # print(s2)
    def __str__(self):  # print(s2)调用
        return f"姓名{self.name},年龄 {self.age}"


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # 放置多继承重复调用(super只调用一次)
        self.school = school
