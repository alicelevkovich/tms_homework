# Print 1 or 5 line
def print_selected_line(file_name: str, line_number: int = 5):
    some_file = open(file_name)
    counter = 0

    while counter != line_number:
        line = some_file.readline()
        if not line:
            print('File size is less than 5')
            break

        if counter + 1 == line_number:
            print(line)

        counter += 1

    some_file.close()


print_selected_line('test_10.txt', line_number=1)


# Print first 5 lines
def print_selected_range_line(file_name: str, number_of_lines: int):
    some_file = open(file_name)
    counter = 0

    while counter < number_of_lines:
        line = some_file.readline()
        print(line.replace('\n', ' '))
        if not line:
            print('File size is less than 5')
            break

        counter += 1

    some_file.close()


print_selected_range_line('test_10.txt', number_of_lines=5)


# Print lines from s1 to s2
def print_range_s1_s2(file_name: str, number_of_first_line: int, number_of_second_line: int):
    some_file = open(file_name)
    counter = 0

    while counter < number_of_second_line:
        if number_of_first_line < number_of_second_line:
            line = some_file.readline()
            print(line.replace('\n', ' '))
        else:
            print('Wrong range')
            break

        counter += 1

    some_file.close()


print_range_s1_s2('test_10.txt', number_of_first_line=7, number_of_second_line=3)


# Print all lines
def print_all_lines(file_name: str):
    some_file = open(file_name)
    line = some_file.readlines()
    result_lines = ''.join(line)

    some_file.close()
    return result_lines


print(print_all_lines('test_10.txt'))
