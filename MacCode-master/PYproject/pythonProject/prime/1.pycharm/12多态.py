class Animal:
    def make_sound(self):
        print("animal")


class Dog(Animal):
    def make_sound(self):
        print("dog")


class Cat(Animal):
    def make_sound(self):
        print("cat")


# 定义统一调用接口
def animal_sound(animal: Animal):
    animal.make_sound()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    animal_sound(dog)
    animal_sound(cat)
