from datetime import datetime


def add_time_decorator(func):
    def add_time():
        time_before = datetime.now()
        func()
        time_after = datetime.now()
        result_time = time_after - time_before
        print(f'This function was executed in: {result_time}')

    return add_time


@add_time_decorator
def original_func():
    print('This is original function')


original_func()
