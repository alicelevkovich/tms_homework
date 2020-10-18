def differences_in_poem(file_to_compare_1: str, file_to_compare_2: str):
    with open(file_to_compare_1) as first_file:
        all_lines_1 = first_file.readlines()
        enumerate_all_lines_1 = list(enumerate(all_lines_1))

    with open(file_to_compare_2) as second_file:
        all_lines_2 = second_file.readlines()
        enumerate_all_lines_2 = list(enumerate(all_lines_2))

        for element in enumerate_all_lines_1:
            i = element[0]
            if element[1] != enumerate_all_lines_2[i][1]:
                line_number = i

    return line_number


print(differences_in_poem('text_10_06_1.txt', 'text_10_06_2.txt'))
