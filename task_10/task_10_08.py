import csv_utils

title = ['Product name', 'Price', 'Amount', 'Comment']
products_info = [
    ['apple', '4', '3', 'golden'],
    ['coffee', '8', '1', 'ethiopia'],
    ['carrot', '12', '32', 'belarus'],
    ['gloves', '4', '43', 'wool'],
    ['bread', '2', '1', 'rye']
]
new_product = ['pen', '6', '23', 'blue']

csv_utils.write_file(file_to_write='text_10_08.csv', fields=title, rows=products_info)
fields, rows = csv_utils.read_file(file_to_read='text_10_08.csv')
rows_add = csv_utils.add_by_position(rows=rows, new_row=new_product)
csv_utils.write_file(file_to_write='text_10_08.csv', fields=fields, rows=rows_add)
rows_del = csv_utils.delete_by_position(rows=rows_add, position=2)
csv_utils.write_file(file_to_write='text_10_08.csv', fields=fields, rows=rows_del)
