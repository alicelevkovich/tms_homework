dict_of_letters = {'upper': 0, 'lower': 0}


# The first variant:

def string_to_dict_first(some_string):
    if not isinstance(some_string, int):
        for element in some_string:
            if element.isupper():
                dict_of_letters['upper'] += 1
            elif element.islower():
                dict_of_letters['lower'] += 1
    else:
        print('This is a number')
    return dict_of_letters


print(string_to_dict_first('GOOD morning'))


# The second variant (using try-except construction):

def string_to_dict_second(some_string):
    try:
        for element in some_string:
            if element.isupper():
                dict_of_letters['upper'] += 1
            elif element.islower():
                dict_of_letters['lower'] += 1
    except TypeError:
        print('This is not a string')
    finally:
        return dict_of_letters


print(string_to_dict_second(32))
