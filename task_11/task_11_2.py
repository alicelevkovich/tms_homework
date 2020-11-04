class Car(object):

    def __init__(self, brand, model, year, velocity: int = 0, coefficient: int = 5):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__velocity = velocity
        self.coefficient = coefficient

    def increase_velocity(self):
        if isinstance(self.__velocity, int):
            self.__velocity += self.coefficient
            return self.__velocity

    def decrease_velocity(self):
        if isinstance(self.__velocity, int):
            self.__velocity -= self.coefficient
            return self.__velocity

    def stop(self):
        if isinstance(self.__velocity, int):
            self.__velocity = 0
            return self.__velocity

    def view_velocity(self):
        if isinstance(self.__velocity, int):
            print(f'Velocity is {self.__velocity}')

    def turn_back(self):
        if isinstance(self.__velocity, int):
            self.__velocity *= (-1)
            return self.__velocity


if __name__ == '__main__':
    car = Car(brand='Volvo', model='c40', year=2010, velocity=40)
    car.increase_velocity()
    car.decrease_velocity()
    car.stop()
    car.view_velocity()
    car.turn_back()
