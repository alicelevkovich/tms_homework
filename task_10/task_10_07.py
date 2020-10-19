import random
import json


def fill_matrix(num_of_rows: int, num_of_columns: int):
    matrix = [[random.randint(0, 40) for i in range(num_of_rows)] for j in range(num_of_columns)]
    return matrix


original_matrix = fill_matrix(num_of_rows=6, num_of_columns=6)

with open('text_10_07.json', 'w') as matrix_file:
    data = json.dumps(original_matrix)
    matrix_file.write(data)


def change_matrix(file_to_change: str):
    with open(file_to_change, 'r+') as matrix_file_for_change:
        file_data = json.loads(matrix_file_for_change.read())
        new_matrix = []
        for element in file_data:
            new_value = []
            for value in element:
                if value % 2 == 0:
                    new_value.append(0)
                else:
                    new_value.append(value)
            new_matrix.append(new_value)
        return new_matrix


changed_matrix = change_matrix(file_to_change='text_10_07.json')


with open('text_10_07_new.json', 'w') as new_json_file:
    data = json.dumps(changed_matrix)
    new_json_file.write(data)


