import click
import requests


@click.command(name="umm")
def umm():
    requests.get()


@click.command(name="umm-start")
def umm_start():
    pass


if __name__ == "__main__":
    umm()
