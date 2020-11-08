from argparse import ArgumentParser
import os

PY_DATA = '''def main():\n\tpass'''
PY_EXPANSION = '.py'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--folder-name', required=True)
    parser.add_argument('-fi', '--file_name', required=True)
    args = parser.parse_args()

    file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(file_path)

    new_dir_abs_path = f'{current_dir}/{args.folder_name}'
    os.mkdir(new_dir_abs_path)

    new_file_path = f'{new_dir_abs_path}/{args.file_name}'
    if args.file_name[-3:] == PY_EXPANSION:
        with open(new_file_path, 'w') as file:
            file.write(PY_DATA)
