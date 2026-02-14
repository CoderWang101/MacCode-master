# class Animal:
#     def make_sound(self):
#         print("animal")


# a1 = Animal()
# a2 = Animal()
# print(id(a1), '\n', id(a2))  # id不同相同
# print(a1 is a2)

class singleton(object):
    _instances = None  # 始终指向同一对象

    # 单例模式:__new__
    def __new__(cls, *args, **kwargs):  # __new__ 的作用是拦截实例化过程，确保整个类只生成一个对象
        if cls._instances is None:
            cls._instances = super().__new__(cls)  # 申请空间
        return cls._instances

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


# 单例模式 # 只能有一个调用(类似于PV)
music_player1 = singleton('爱拼才会赢')
music_player2 = singleton('雇用者')

print(id(music_player1), '\n', id(music_player2))  # id相同
print(music_player1)  # 雇用者 #(music_player2)
print("is 判断是否指向同一个空间")
print("music_player1与usic_player2是否是同一空间:", music_player1 is music_player2)
