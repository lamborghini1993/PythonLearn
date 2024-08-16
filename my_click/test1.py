"""
https://click-docs-zh-cn.readthedocs.io/zh/latest/options.html
"""

import click


@click.command()
def hello():
    click.echo("Hello World!")


@click.command()  # 定义一个命令
@click.argument("name")  # 使用参数，name为用户输入的参数
def greet(name):
    """该命令用来问候特定的人"""  # 命令的帮助信息
    click.echo(f"Hello, {name}!")  # 打印概定的问候语


@click.command()  # 定义一个命令
@click.option("--count", default=1, help="问候的次数")  # 定义选项，可以控制问候的次数
def repeat_greet(count):
    """该命令可重复问候用户"""  # 命令的帮助信息
    for _ in range(count):  # 循环次数由用户指定
        click.echo("Hello, User!")  # 打印问候语


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello2(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo("Hello %s!" % name)


@click.command()
@click.argument("value", type=click.Choice(["a", "b", "c"]))
def test_argument(value):
    """
    测试命令行参数
    """
    click.echo(f"test_argument {value}-{type(value)}")


@click.command()
@click.option("--message", "-m", multiple=True)
def commit(message):
    """一个参数传递多次"""
    click.echo("\n".join(message))


if __name__ == "__main__":
    # hello()
    # greet()
    # repeat_greet()
    # hello2()
    # test_argument()
    commit()
