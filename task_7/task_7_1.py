from random import randint

original_list = []
for index in range(1, 10):
    list_element = randint(1, 100)
    original_list.append(list_element)
list_of_unique = []


def unique(list_):
    for number in list_:
        if number not in list_of_unique:
            list_of_unique.append(number)
    return list_of_unique


print(f'Список уникалных значений: {unique(original_list)}')
