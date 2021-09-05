import subprocess

import click
from pygments import console


@click.command()
@click.option("--start", "-s", is_flag=True)
@click.option("--copy", "-c", is_flag=True)
@click.argument("tags", nargs=-1)
def umm(start, copy, tags):
    if start:
        print("umm server starting")
        # start server

    print(tags)

    for i in range(10):
        msg = console.colorize("green", f"is {i} right?")
        if click.confirm(msg, default=True):
            break

    # if command has prompts
    # collect prompts in

    # build command

    if copy:
        subprocess.run([f"echo command: {i} |pbcopy"], shell=True)
    else:
        subprocess.run([f"command: {i}"])
