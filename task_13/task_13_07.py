from random import randint
from typing import Optional, List


class Matrix:

    # data, n, m = None, None, None

    def __init__(self, n=5, m=5, a=0, b=0, data: Optional[List] = None):
        self.n = n
        self.m = m
        self.a = a
        self.b = b

        self.data = data if data else [[randint(a, b) for i in range(n)] for j in range(m)]

    # Implementation of copy method using staticmethod

    # @staticmethod
    # def copy_constructor(matrix):
    #     new_object = Matrix(n=matrix.n, m=matrix.m, a=matrix.a, b=matrix.b)
    #     new_object.data = matrix.data
    #     return new_object

    def __copy__(self):
        return Matrix(n=self.n, m=self.m, a=self.a, b=self.b, data=self.data)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


def max_elem(matr: Matrix):
    elem_to_compare = matr.data[0][0]
    for element in matr.data:
        for num in element:
            if num > elem_to_compare:
                elem_to_compare = num
    return elem_to_compare


def min_elem(matr: Matrix):
    elem_to_compare = matr.data[0][0]
    for element in matr.data:
        for num in element:
            if num < elem_to_compare:
                elem_to_compare = num
    return elem_to_compare


def sum_elem(matr: Matrix):
    sum_ = 0
    for element in matr.data:
        for num in element:
            sum_ += num
    return sum_
