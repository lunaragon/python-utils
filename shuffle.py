import fire
import sys
import pathlib
import random


CWD = pathlib.Path.cwd()


def shuffle(input_file, output_file):
    input_file_path = CWD / input_file
    output_file_path = CWD / output_file

    # parameter check
    if input_file_path.is_file() is not True:
        sys.exit('{path} is not a file'.format(path=input_file))
    if output_file_path.is_file() is not True:
        sys.exit('{path} is not a file'.format(path=output_file))

    # read input_file into a dict
    inputs = {}
    index = 1
    for line in open(input_file_path, 'r', encoding='utf8'):
        inputs[index] = line
        index += 1

    print('read finished')

    # write output
    index_list = [i for i in range(index)]
    random.shuffle(index_list)


def main():
    fire.Fire(shuffle)


if __name__ == '__main__':
    sys.exit(main())
