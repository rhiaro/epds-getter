import os
import click
import dataset

from epdsgetter.getter import get_local_data, countdata

@click.group()
def cli():
    pass


@cli.command()
def get():
    data = get_local_data()
    click.echo(len(data))


@cli.command()
def count():
    click.echo('There are %s rows in the database' % countdata())


@cli.command()
def flush():
    click.echo('Emptying the database')
