from argparse import ArgumentParser
import os

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--folder-name', required=True)
    parser.add_argument('-fi', '--file_name', required=True)
    args = parser.parse_args()

    file_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(file_path)
    os.mkdir(f'{dir_name}/{args.folder_name}')
    file_name = 'new_file_1'
    with open(f'{dir_name}/{args.folder_name}/{file_name}', 'w') as new_file:
        new_file.write(' ')
