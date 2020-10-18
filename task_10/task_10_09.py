import csv_utils
from typing import List
from functools import reduce

fields, rows = csv_utils.read_file(file_to_read='text_10_08.csv')


# function of calculating the total amount of all products
def reducer_func(prev_elem, elem):
    return prev_elem + elem


prices = list(map(lambda x: int(x[1]), rows))
sum_ = reduce(reducer_func, prices)
print(sum_)


# search function for the most expensive product
def expensive_product(max_price, price):
    return price if price > max_price else max_price


max_ = reduce(expensive_product, prices, prices[0])
print(max_)


# function of the cheapest product
def cheapest_product(min_price, price):
    return price if price < min_price else min_price


min_ = reduce(cheapest_product, prices, prices[0])
print(min_)


# the function of decreasing the quantity of products (by n, default by 1)
def decrease_amount(product: list, decrease_index=1):
    product[2] = int(product[2]) - decrease_index
    return product


print(decrease_amount(rows[2]))
