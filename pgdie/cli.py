# -*- coding: utf-8 -*-

import click

@click.command()
def config():
    pass


@click.command()
@click.argument('command', required=False)
@click.pass_context
def help(ctx, command):
    pass


@click.command()
def dump():
    pass


@click.command()
def load():
    pass


if __name__ == "__main__":
    help()
