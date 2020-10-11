list_of_numbers = [3, 45, 6, 4, 54, 3, 35, 2, 943, 456, 854, 2, 54, 95, 67, 90]


def data_checking_decorator(func):
    def to_check_list(list_of_num):
        filtered_list = filter(lambda element: element % 2 != 0, list_of_num)
        func(list_of_num)
        return filtered_list
    return to_check_list


@data_checking_decorator
def original_func(list_of_num):
    print(list_of_num)


result = original_func(list_of_numbers)
print(list(result))
