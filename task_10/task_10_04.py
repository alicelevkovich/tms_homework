def replace_elements(file_to_read: str, file_to_write: str):
    elements_to_write = []
    with open(file_to_read, 'r+') as file_1:
        all_lines = file_1.readlines()

        for line in all_lines:
            new_line = ''

            for char in line:
                if char == '0':
                    new_line += '1'
                elif char == '1':
                    new_line += '0'
                else:
                    new_line += char
                # new_line += '0' if char == '1' else '1' if char == '0' else char

            elements_to_write.append(new_line)

    with open(file_to_write, 'w') as file_2:
        file_2.writelines(elements_to_write)


replace_elements('text_04_1.txt', 'text_04_2.txt')
