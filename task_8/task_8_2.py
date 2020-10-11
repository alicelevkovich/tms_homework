dict_with_doublekey = lambda **kwargs: {key * 2: value for (key, value) in kwargs.items()}

print(dict_with_doublekey(a=5, b='f'))
