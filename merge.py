"""Merge files or directory into one single file\n
Example\n
\tpython merge.py file1, file2, [file3, file4,] merged_file\n
\tpython merge.py dir1, [dir2, dir3,] merged_file
"""
import click
import pathlib

CWD = pathlib.Path.cwd()


@click.command()
@click.argument('items', nargs=-1, type=str)
@click.argument('merged_file', nargs=1, type=click.File('wb'))
@click.option('--recur', is_flag=True, default=False,
    help='merge content in child directory, default=False')
def merge(items, merged_file, recur):
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
            merge_dir(item, merged_file, recur)
        elif item.is_file():
            merge_file(item, merged_file)
        else:
            click.secho('[Warning] {item} skiped, non file nor directory'.format(
                item=item.name
            ), fg='yellow', bold=True)
        

def merge_dir(dir_path, merged_file, recur):
    for item in dir_path.iterdir():
        if item.is_file():
            merge_file(item, merged_file)
        elif item.is_dir():
            if recur:
                merge_dir(item, merged_file, recur) # recure call
            else:
                click.secho('[Warning] skiped child directory {item}'.format(
                    item=item.name
                ), fg='yellow', bold=True)
        else:
            pass

def merge_file(file_path, merged_file):
    [merged_file.write(line) for line in open(file_path, 'rb')]
    click.secho('Merged {file} into {merged}'.format(
            file=file_path,
            merged=merged_file.name
        ), fg='green', bold=True)


if __name__ == '__main__':
    merge()
