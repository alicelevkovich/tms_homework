import csv
from typing import List

__all__ = [
    'read_file',
    'write_file',
    'add_by_position',
    'delete_by_position'
]


# Read csv file
def read_file(*, file_to_read: str):
    rows = []
    with open(file_to_read, 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return fields, rows


# Write csv file
def write_file(*, file_to_write: str, fields: List, rows: List[List]):
    with open(file_to_write, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


# Adding a record by position, to the end(by default)
def add_by_position(*, rows: List, position=None, new_row: List):
    if isinstance(new_row, list):
        if position is not None:
            rows.insert(position, new_row)
        else:
            rows.append(new_row)
    else:
        print("Please, enter list")
    return rows


# Deleting of a record by position, to the end (by default)
def delete_by_position(*, rows: List, position=None):
    if position is not None:
        rows.pop(position)
    else:
        rows.pop()
    return rows
