def write_lines(file_name: str):
    with open(file_name, 'a') as my_file:
        for _ in range(3):
            input_string = input('Enter your string: ')
            my_file.write(input_string + '\n')


write_lines('test_10_1.txt')
