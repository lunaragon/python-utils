"""
# 从指定文件中随机取出一定行数 line_number, valued from 0 to file lines
python shuffle.py --input-file input_file --output-file output_file --number line_number
# 从指定文件中随机取出一定百分比的内容 (按行):  percent, valued from 0 to 1
python shuffle.py --input-file input_file --output-file output_file --percent percent
# 未指定行数与百分比，则将原文本打乱
python shuffle.py --intput-file input_file --output-file output_file
"""

import fire
import sys
import pathlib
import random


CWD = pathlib.Path.cwd()


class Shuffler():
    """Implementation of this script
    """

    def __init__(self, input_file, output_file):
        # parameter check
        input_file_path = CWD / input_file
        output_file_path = CWD / output_file

        if not input_file_path.is_file():
            raise TypeError('{name} is not a file.'.format(name=input_file_path.name)) 

        self.input_file_path = input_file_path
        self.line_number = len(["" for line in open(input_file_path, 'r', encoding='utf8')])


    def by_line_number(self, line_number=None):
        
        file_dict = {index:line 
            for index, line in enumerate(
                open(self.input_file_path, 'r', encoding='utf8'), 1)}
        print(file_dict)
        if not line_number:
            # just shuffle
            pass



    def by_percent(self, percent=1):
        pass


# Script start
def main():
    fire.Fire(Shuffler)


if __name__ == '__main__':
    sys.exit(main())
