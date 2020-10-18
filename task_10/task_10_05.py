def is_even_lines(file_to_read: str, file_to_write_even: str, file_to_write_odd: str):
    even_elements = []
    odd_elements = []
    with open(file_to_read, 'r+') as original_file:
        all_lines = original_file.readlines()
        enumerate_lines = enumerate(all_lines)

        for i, line in enumerate_lines:
            if i % 2 == 0:
                even_elements.append(line)
            elif i % 2 != 0:
                odd_elements.append(line)

    with open(file_to_write_even, 'w') as even_file:
        even_file.writelines(even_elements)
    with open(file_to_write_odd, 'w') as odd_file:
        odd_file.writelines(odd_elements)


is_even_lines('test_10.txt', 'even_10.txt', 'odd_10.txt')
