from typing import List
import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(object):

    def side_length(self, point_1, point_2):
        ab_square = pow((point_2.x - point_1.x), 2) + (pow((point_2.y - point_1.y), 2))
        ab = math.sqrt(ab_square)
        return ab


class Circle(Figure):

    def __init__(self, radius, point):
        self.point = point
        self.radius = radius

    def circle_length_calc(self):
        circle_length = 2 * math.pi * self.radius
        return circle_length

    def square_calc(self):
        circle_square = math.pi * pow(self.radius, 2)
        return circle_square


class Triangle(Figure):

    def __init__(self, p_1, p_2, p_3):
        self.point_1 = p_1
        self.point_2 = p_2
        self.point_3 = p_3

    def ab_side(self):
        ab = self.side_length(self.point_1, self.point_2)
        return ab

    def bc_side(self):
        bc = self.side_length(self.point_2, self.point_3)
        return bc

    def ca_side(self):
        ca = self.side_length(self.point_3, self.point_1)
        return ca

    def perimeter_triangle_calc(self):
        perimeter_triangle = self.ab_side() + self.bc_side() + self.ca_side()
        return perimeter_triangle

    def square_calc(self):
        squared_expression = (self.perimeter_triangle_calc() / 2 * (self.perimeter_triangle_calc() / 2 - self.ab_side())
                              * (self.perimeter_triangle_calc() / 2 - self.bc_side())
                              * (self.perimeter_triangle_calc() / 2 - self.ca_side())
                              )
        square_triangle = math.sqrt(squared_expression)
        return square_triangle


class Square(Figure):
    def __init__(self, p_1, p_2):
        self.point_1 = p_1
        self.point_2 = p_2

    def perimeter_square_calc(self):
        perimeter_square = 4 * self.side_length(self.point_1, self.point_2)
        return perimeter_square

    def square_calc(self):
        square_of_square = pow(self.side_length(self.point_1, self.point_2), 2)
        return square_of_square

