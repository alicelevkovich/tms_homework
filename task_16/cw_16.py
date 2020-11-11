storage = {}


def hash_func_decorator(func):
    def remember_result(a, b):
        tuple_of_arguments = (a, b)
        if tuple_of_arguments not in storage.keys():
            result = func(a, b)
            storage[tuple_of_arguments] = result
            return result
        else:
            return storage[tuple_of_arguments]
    return remember_result


@hash_func_decorator
def some_sum(a, b):
    sum_ = a + b
    return sum_


print(some_sum(3, 5))
print(some_sum(3, 5))


