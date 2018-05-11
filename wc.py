"""Count file lines
python wc.py file [file2] [file3]
python wc.py dir [--depth n]
"""


import pathlib
import click


CWD = pathlib.Path.cwd()

@click.command()
@click.argument('items', nargs=-1)
@click.option('--depth', is_flag=True, default=False,
    help='merge content in child directory, default=False')
def count_line(items, depth):
    sums = 0
    for item in items:
        item_path = CWD / item
        if item_path.is_file():
            line = count_file_line(item_path)
            sums += line
            click.secho('{filename}\t{line}'.format(
                filename=item,
                line=line
            ), fg='green', bold=True)
        elif item_path.is_dir():
            line = count_dir_line(item_path)
            sums += line
                

def count_dir_line(dir_path):
    for child in dir_path.iterdir():
        if child.is_file():
            count_file_line(child)
        elif child.is_dir():
            count_dir_line(dir_path)
        else:
            continue


def count_file_line(file_path):
    empty_assistant_list = ["" for line in open(file_path, "rb")]
    return len(empty_assistant_list)

if __name__ == '__main__':
    count_line()
