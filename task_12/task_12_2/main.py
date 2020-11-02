from classes import Point, Circle, Triangle, Square

point_1 = Point(-2, 2)
point_2 = Point(3, 2)
point_3 = Point(-1, 0)

circle = Circle(6, point_1)
triangle = Triangle(point_1, point_2, point_3)
square = Square(point_1, point_2)

figures_list = [circle, triangle, square]

for element in figures_list:
    print(element.square_calc())

