"""
# example
python text_merge.py [file1, file2, file3...] merged_file
python text_merge.py --dir dir merged_file
"""
import sys
import pathlib
import fire

# Path configuration
CWD = pathlib.Path.cwd()


def MergeByDir(direcotry, merged_file):
    dir_path = CWD / direcotry
    merged_file_path = CWD / merged_file

    merged_file = open(merged_file_path, 'w', encoding='utf8')
    
    if not dir_path.is_dir():
        return '{name} is not a directory'.format(name=dir_path.name)
    
    for file_path in dir_path.iterdir():
        file_name = file_path.name
        if not file_path.is_file():
            print('{name} is a directory, skipped...'.format(name=file_name))
            continue

        for line in open(file_path, 'r', encoding='utf8'):
            merged_file.write(line)
        
        print('{name} finished merge.'.format(name=file_name))
        


def MergeByFiles(*args):
    # used by multi files method
    if len(args) < 3:
        return 'At lease provide two files to merge...'
    input_file_paths = [CWD / path for path in args[:-1]]
    merged_file_path = CWD / args[-1]

    # parameter check
    for file_path in input_file_paths:
        if not file_path.is_file():
            return '{name} is not a file.'.format(name=file_path.name)

    merged_file = open(merged_file_path, 'w', encoding='utf8')
    for file_path in input_file_paths:
        for line in open(file_path, 'r', encoding='utf8'):
            merged_file.write(line)
        print('{name} finished merge.'.format(name=file_path.name))
    return 'Done.'


def main():
    fire.Fire({
        'by-files':MergeByFiles,
        'by-dir':MergeByDir
    })


if __name__ == '__main__':
    sys.exit(main())
