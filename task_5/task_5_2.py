# Если не использовать вложенные циклы:

for stars in range(5):
    print(stars * '*')
for stars in range(5, 0, -1):
    print(stars * '*')


# Если использовать вложенные циклы:

for strings in range(5):
    for stars in range(strings):
        print('*', end='')
    print(end='\n')
for strings in range(5, 0, -1):
    for stars in range(strings):
        print('*', end='')
    print(end='\n')