from functools import reduce

list_of_num = [4, 54, 3, 35, 2, 943, 456, 854, 2, 54, 95, 67, 90]
filtered_number = filter(lambda element: element % 3 == 0, list_of_num)
# После выполнения filter() список очищается?
# print(list(filtered_number))
# print(list(filtered_number))
multiple_number = reduce(lambda prev_elem, curr_element: prev_elem * curr_element, filtered_number, 1)
print(multiple_number)
