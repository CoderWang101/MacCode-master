class car:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'{self.name} is run')
        self.sound()

    def sound(self):
        print(f'{self.name} is sound')

tengshi = car("腾势")
wenjie=car("问界")

tengshi.run()
wenjie.run()
s1=car(" ")
s1.name="小米"
s1.run()