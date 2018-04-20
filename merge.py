"""Merge files or directory into one single file
Example\n
\tpython merge.py file1, file2, [file3, file4,] merged_file
\tpython merge.py dir1, [dir2, dir3,] merged_file
"""
import click
import pathlib

CWD = pathlib.Path.cwd()


@click.command()
@click.argument('items', nargs=-1, type=str)
@click.argument('merged_file', nargs=1, type=click.File('wb'))
def merge(items, merged_file):
    """Merge files or directory into one single file\n
    Example\n
    \tpython merge.py file1, file2, [file3, file4,] merged_file\n
    \tpython merge.py dir1, [dir2, dir3,] merged_file
    """

    item_path = [ CWD / item for item in items]
    # paramter check
    if len(item_path) == 1 and item_path[0].is_file():
        return click.secho('[Kidding] Do you think this operation is merge?', fg='yellow', bold=True)
    
    for item in item_path:
        if item.is_dir():
            merge_dir(item, merged_file)
        elif item.is_file():
            merge_file(item, merged_file)
        else:
            click.secho('[Warning] {item} skiped, non file nor directory'.format(
                item=item.name
            ), fg='yellow', bold=True)

    print('Merged', ', '.join(items), 'into ', merged_file.name)


def merge_dir(dir_path, merged_file):
    for item in dir_path.iterdir():
        if item.is_file():
            merge_file(item, merged_file)
        elif item.is_dir():
            merge_dir(item, merged_file) # recure call 


def merge_file(file_path, merged_file):
    [merged_file.write(line) for line in open(file_path, 'rb')]


if __name__ == '__main__':
    merge()
