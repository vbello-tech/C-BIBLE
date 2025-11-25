
import click

from .bible import cbible, request, find


@click.group()
def bible():
    pass


bible.add_command(cbible)
bible.add_command(request)
bible.add_command(find)


if __name__ == '__main__':
    bible()
