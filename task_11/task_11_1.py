class Animals(object):

    def __init__(self, name, height, weight, age, habitat):
        self._name = name
        self._height = height
        self._weight = weight
        self._age = age
        self._habitat = habitat


class Giraffe(Animals):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(self._name, str):
            self._name = name
        else:
            print('Wrong instance of name')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height in range(0, 100):
            self._height = height
        else:
            print('Impossible height')

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight in range(0, 50):
            self._weight = weight
        else:
            print('You out of the range of weight')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            print('Enter the number')

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        if isinstance(self._habitat, str):
            self._habitat = habitat
        else:
            print('Your enter do not looks like a string')

    def food(self):
        print(f'{self._name} eat leaves')

    def color(self):
        print(f'{self._name} has a color of light brown spots')


class Elephant(Animals):

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            if isinstance(name, str):
                self._name = name
            else:
                print('Wrong instance of name')

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, height):
            if height in range(0, 100):
                self._height = height
            else:
                print('Impossible height')

        @property
        def weight(self):
            return self._weight

        @weight.setter
        def weight(self, weight):
            if weight in range(0, 50):
                self._weight = weight
            else:
                print('You out of the range of weight')

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, age):
            if isinstance(age, int):
                self._age = age
            else:
                print('Enter the number')

        @property
        def habitat(self):
            return self._habitat

        @habitat.setter
        def habitat(self, habitat):
            if isinstance(habitat, str):
                self._habitat = habitat
            else:
                print('Your enter do not looks like a string')

        def food(self):
            print(f'{self._name} eat leaves and grass')

        def color(self):
            print(f'{self._name} is gray')


class Puma(Animals):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print('Wrong instance of name')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height in range(0, 100):
            self._height = height
        else:
            print('Impossible height')

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight in range(0, 50):
            self._weight = weight
        else:
            print('You out of the range of weight')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            print('Enter the number')

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        if isinstance(habitat, str):
            self._habitat = habitat
        else:
            print('Your enter do not looks like a string')

    def food(self):
        print(f'{self._name} carnivorous')

    def color(self):
        print(f'{self._name} is sand')


class Rabbit(Animals):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print('Wrong instance of name')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height in range(0, 100):
            self._height = height
        else:
            print('Impossible height')

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight in range(0, 50):
            self._weight = weight
        else:
            print('You out of the range of weight')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            print('Enter the number')

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        if isinstance(habitat, str):
            self._habitat = habitat
        else:
            print('Your enter do not looks like a string')

    def food(self):
        print(f'{self._name}  herbivore')

    def color(self):
        print(f'{self._name} is gray or white')


class Lion(Animals):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print('Wrong instance of name')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height in range(0, 100):
            self._height = height
        else:
            print('Impossible height')

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight in range(0, 50):
            self._weight = weight
        else:
            print('You out of the range of weight')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            print('Enter the number')

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, habitat):
        if isinstance(habitat, str):
            self._habitat = habitat
        else:
            print('Your enter do not looks like a string')

    def food(self):
        print(f'{self._name}  carnivorous')

    def color(self):
        print(f'{self._name} is yellow')


if __name__ == '__main__':
    giraffe = Giraffe(name='Edd', height=40, weight=30, age=13, habitat='Africa')
    elephant = Elephant(name='Audrie', height=55, weight=45, age=30, habitat='Southeast Asia and Africa')
    puma = Puma(name='Carlie', height=20, weight=14, age=4, habitat='North and South America')
    rabbit = Rabbit(name='Tailor', height=5, weight=6, age=3, habitat='Everywhere')
    lion = Lion(name='Rick', height=24, weight=20, age=8, habitat='Africa')
    giraffe.color()
    puma.food()
