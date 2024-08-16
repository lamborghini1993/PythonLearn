import click


@click.group()
def cli():
    pass


@cli.command()
def test1():
    click.echo("test1")


@cli.command()
def test2():
    click.echo("test2")


@cli.command()
@click.argument("name")
@click.option("--count", default=2, help="重复次数")
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}")


if __name__ == "__main__":
    cli()
