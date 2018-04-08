"""
# 从指定文件中随机取出一定行数 line_number, valued from 0 to file lines
python shuffle.py
    --input-file input_file
    --output-file output_file
    by-line-number --number line_number
# 从指定文件中随机取出一定百分比的内容 (按行):  percent, valued from 0 to 1
python shuffle.py
    --input-file input_file
    --output-file output_file
    --by-percent percent
# 未指定行数与百分比，则将原文本打乱
python shuffle.py
    --intput-file input_file
    --output-file output_file
    --by-line-number/--by-percent
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
            raise TypeError('{name} is not a file.'.format(
                name=input_file_path.name))

        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.line_number = len(["" for line in open(
            input_file_path, 'r', encoding='utf8')])

    def by_line_number(self, line_number=None):
        output_file = open(self.output_file_path, 'w', encoding='utf8')
        file_dict = {index: line
                     for index, line in enumerate(
                         open(self.input_file_path, 'r', encoding='utf8'))}
        shuffle_list = [x for x in range(self.line_number)]
        random.shuffle(shuffle_list)

        # havn't specify line number, just shuffle the file
        if not line_number or line_number == self.line_number:
            for index in shuffle_list:
                output_file.write(file_dict[index])
        elif line_number > 0 and line_number < self.line_number:
            for index, val in enumerate(shuffle_list):
                # write line_number lines file
                if index > line_number:
                    break
                output_file.write(file_dict[val])
        else:
            raise ValueError('line number should less than {0}, not {1}'
                             .format(self.line_number, line_number))

    def by_percent(self, percent=None):
        if not percent or percent == 1:
            self.by_line_number()
        elif percent > 0 and percent < 1:
            self.by_line_number(round(percent * self.line_number))
        else:
            raise ValueError('Percent should valued from 0 to 1, not {percent}'
                             .format(percent=percent))


# Script start
def main():
    fire.Fire(Shuffler)


if __name__ == '__main__':
    sys.exit(main())
