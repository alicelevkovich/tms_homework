import classes

point_1 = classes.Point(-2, 2)
point_2 = classes. Point(3, 2)
point_3 = classes.Point(-1, 0)

circle = classes.Circle(6, point_1)
triangle = classes.Triangle(point_1, point_2, point_3)
square = classes.Square(point_1, point_2)

figures_list = [circle, triangle, square]

for element in figures_list:
    print(element.square_calc())



