class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__balance = 0  # 双'_'表示private

    def __str__(self):
        return f'{self.name} {self.age} {self.__balance}'

    def __address(self):  # 内部类只能再类内部调用
        return
        # 提供借口查看余额

    def get_balance(self):
        return self.__balance

    # 进行存款业务
    def set_balance(self, balance):
        self.__balance += balance
        print("存钱成功,存", self.__balance)

    # 进行取款业务
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
        else:
            print("余额不足,取钱失败")


if __name__ == '__main__':
    s1 = Person("小明", 12)
    s1.set_balance(100)
    s1.withdraw(1000)
