class Pet(object):
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = int(age)
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print(f'{self.name}, run!')

    def jump(self):
        print(f'{self.name}, jump!')

    def birthday(self):
        self.age += 1
        print(f'{self.name} is {self.age}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def change_weight(self, weight, int=0.2):
        self.weight += weight

    def change_height(self, height, int=0.2):
        self.weight += height


class Dog(Pet):
    def bark(self):
        print(f'{self.name}, bark!')


class Cat(Pet):
    def meow(self):
        print(f'{self.name}, meow!')


class Parrot(Pet):
    def fly(self):
        print(f'{self.name}, fly!')


dog = Dog(name='Charlie', age='5', master='Ivan')
dog.jump()
dog.run()
dog.birthday()
dog.sleep()
dog.bark()

cat = Cat(name='Oskar', age='4', master='Elon')
cat.jump()
cat.run()
cat.birthday()
cat.sleep()
cat.meow()

parrot = Parrot(name='Buffy', age='2', master='Maya')
parrot.jump()
parrot.run()
parrot.birthday()
parrot.sleep()
parrot.fly()
