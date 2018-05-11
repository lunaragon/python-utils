"""Split a file into multi files, split by line or fixed line number.
If --output option was not set, script will create a directory named as 
split_file in current working directory\n
Example\n
\tpython split.py file by-line lineNumber\n
\tpython split.py file by-filenumber fileNumber\n
\tpython split.py file by-line lineNumber --output dir_name\n
"""
import click
import pathlib
import sys

CWD = pathlib.Path.cwd()

@click.command()
@click.argument('split_file', nargs=1, type=str)
@click.argument('split_method', nargs=1, type=str)
@click.argument('number', nargs=1, type=int)
@click.option('--outputdir', type=str, help='Output directory')
def split(split_file, split_method, number, outputdir):
    """Split a file into multi files, split by line or fixed line number.
    If --output option was not set, script will create a directory named as 
    file_split in current working directory\n
    Example\n
    \tpython split.py file by-line lineNumber\n
    \tpython split.py file by-filenumber fileNumber\n
    \tpython split.py file by-line lineNumber --output dir_name\n
    """

    split_file_path = CWD / split_file
    
    if not split_file_path.is_file():
        return click.secho('{file} is not a file'.format(
            file=split_file_path.name
        ), fg='red', bold=True)

    if not outputdir:
        outputdir = CWD / '{file_name}_split'.format(
            file_name=split_file_path.name[:len(split_file_path.name)-len(split_file_path.suffix)])
    else:
        outputdir = CWD / outputdir

    # check split method and dispatch job
    if split_method == 'by-linenumber':
        splitByLine(split_file_path, number, outputdir)
    elif split_method == 'by-filenumber':
        splitByFileNumber(split_file_path, number, outputdir)
    else:
        return click.secho(('[ERROR] Invalid split method: {wrong}'
        '\n\tChoose from by-linenumber, by-filenumber').format(
            wrong=split_method
        ), fg='red', bold=True)


def splitByLine(split_file, number, outputdir):
    if not outputdir.exists():
        outputdir.mkdir()
    
    # initialization
    file_name = split_file.name
    output_file_index = 1
    input_file = open(split_file, 'r', encoding='utf8')

    def read_and_write(output_file_index):
        # configure output file
        output_file_path = outputdir / '{index}_{filename}'.format(
            index=output_file_index, filename=file_name)
        output_file = open(output_file_path, 'w', encoding='utf8')

        # read and write line_number lines every time
        for line_index in range(number):
            line = input_file.readline()

            if line == '':
                output_file.close()
                raise EOFError('Finished.')

            output_file.write(line)
        # close file
        output_file.close()

    # start job
    while True:
        try:
            read_and_write(output_file_index)
            output_file_index += 1
        except EOFError as ex:
            sys.exit(click.secho('Finished. Totally split into {number} files'.format(
                number=output_file_index
            ), fg='green', bold=True))


def splitByFileNumber(split_file, number, outputdir):
    # get total line numbers
    total_line_number = len(["" for line in open(split_file, 'rb')])
    # call function splitByLine
    return splitByLine(split_file, total_line_number // number + 1, outputdir)


if __name__ == '__main__':
    split()
