"""
# 按固定行数拆分, 指定 --line_number 参数
python text_split.py
    --input-file input_file
    --output-dir output_dir
    --by-line-number line_number
# 按文件个数拆分, 指定 --file_number 参数
python text_split.py
    --input-file input_file
    --output-dir output_dir
    --by-file-number file_number
"""
import os
import pathlib
import sys

import fire

# Path configuration
CWD = pathlib.Path.cwd()
PROJECT_PATH = pathlib.Path(os.path.abspath(__file__)).parent


class TextSpliter(object):
    """Split Text by line-number or file-number
    """
    def __init__(self, input_file, output_dir):
        self.input_file = CWD / input_file
        self.output_dir = CWD / output_dir

        # check parameter
        if self.input_file.is_file() is not True:
            raise TypeError('{0} is not a file.'.format(input_file))
        if self.output_dir.exists() is True:
            if self.output_dir.is_dir() is not True:
                raise TypeError('{0} is not a dir.'.format(output_dir))
        else:
            self.output_dir.mkdir()

    def by_line_number(self, line_number):
        # initialization
        file_name = self.input_file.name
        output_file_index = 1
        input_file = open(self.input_file, 'r', encoding='utf8')

        def read_and_write(output_file_index):
            # configure output file
            output_file_path = self.output_dir / '{index}_{filename}'.format(
                index=output_file_index, filename=file_name)
            output_file = open(output_file_path, 'w', encoding='utf8')

            # read and write line_number lines every time
            for line_index in range(line_number):
                line = input_file.readline()

                if line == '':
                    output_file.close()
                    raise EOFError(
                        'Finished. Totally splited into {number} files'.format(
                            number=output_file_index))

                output_file.write(line)
            # close file
            output_file.close()

        # start job
        while True:
            try:
                read_and_write(output_file_index)
                output_file_index += 1
            except EOFError as ex:
                sys.exit(print(ex))

    def by_file_number(self, file_number):
        # get total line numbers
        total_line_number = len(
            ["" for line in open(self.input_file, 'r', encoding='utf8')])
        # call function by_line_number
        return self.by_line_number(total_line_number // file_number + 1)


def main():
    fire.Fire(TextSpliter)


if __name__ == '__main__':
    sys.exit(main())
