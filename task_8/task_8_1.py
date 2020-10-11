cities = ['Brest', 'Slonim', 'Bereza', 'Mikashevichy', 'Grodno', 'Lida', 'Malorita']


def format_string(some_list):
    for i, city in enumerate(cities):
        new_string = f'{i} - {city}'
        yield new_string


new_list = format_string(cities)
print(next(new_list))
print(next(new_list))
print(next(new_list))
