from task_13_07 import Matrix, max_elem, min_elem, sum_elem
from copy import copy

Matrix()
matrix = Matrix(n=2, m=3, a=2, b=6)
print(matrix)
print(max_elem(matrix))
print(min_elem(matrix))
print(sum_elem(matrix))

new_matrix = copy(matrix)
print(new_matrix)
