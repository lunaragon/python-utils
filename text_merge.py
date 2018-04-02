"""
# example
python text_merge.py [file1, file2, file3...] merged_file
"""
import sys
import pathlib
import fire

# Path configuration
CWD = pathlib.Path.cwd()


def TextMerge(*args):
    if len(args) < 3:
        return 'At lease provide two files to merge...'
    input_file_paths = [CWD / path for path in args[:-1]]
    merged_file_path = CWD / args[-1]

    # parameter check
    for file_path in input_file_paths:
        if file_path.is_file() is not True:
            return '{name} is not a file.'.format(name=file_path.name)

    merged_file = open(merged_file_path, 'w', encoding='utf8')
    for file_path in input_file_paths:
        for line in open(file_path, 'r', encoding='utf8'):
            merged_file.write(line)
        print('{name} finished.'.format(name=file_path.name))
    return 'Done.'


def main():
    fire.Fire(TextMerge)


if __name__ == '__main__':
    sys.exit(main())
