def changing_order_decorator(func):
    def change_order(*args):
        new_args = args[::-1]
        return func(new_args)
    return change_order


@changing_order_decorator
def original_func(*args):
    print(f'Original args {args}')


result = original_func(1, 2, 3)
print(f'Reversed args {result}')
