class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = int(age)
        self.master = master

    def run(self):
        print(f'{self.name}, run!')

    def jump(self):
        print(f'{self.name}, jump!')

    def birthday(self):
        self.age += 1
        print(f'{self.name} is {self.age}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def bark(self):
        print(f'{self.name}, bark!')


class Cat:

    def __init__(self, name, age, master):
        self.name = name
        self.age = int(age)
        self.master = master

    def run(self):
        print(f'{self.name}, run!')

    def jump(self):
        print(f'{self.name}, jump!')

    def birthday(self):
        self.age += 1
        print(f'{self.name} is {self.age}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def meow(self):
        print(f'{self.name}, meow!')


class Parrot:

    def __init__(self, name, age, master):
        self.name = name
        self.age = int(age)
        self.master = master

    def run(self):
        print(f'{self.name}, run!')

    def jump(self):
        print(f'{self.name}, jump!')

    def birthday(self):
        self.age += 1
        print(f'{self.name} is {self.age}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def fly(self):
        print(f'{self.name}, fly!')


dog = Dog(name='Charlie', age='5', master='Ivan')
dog.jump()
dog.run()
dog.birthday()
dog.sleep()
dog.bark()

cat = Cat(name='Oskar', age='4', master='Ilon')
cat.jump()
cat.run()
cat.birthday()
cat.sleep()
cat.meow()


parrot = Parrot(name='Baffie', age='2', master='Maya')
parrot.jump()
parrot.run()
parrot.birthday()
parrot.sleep()
parrot.fly()

