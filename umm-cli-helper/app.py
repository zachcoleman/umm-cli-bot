import logging
import os
import subprocess
import sys

import click
from flask import Flask, g
from utils import parse_commands

logger = logging.getLogger(__file__)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
app = Flask(__name__)


def get_db():
    if "commands" not in g:
        g.commands = parse_commands("resources/commands.yaml")
    return g.commands


@app.teardown_appcontext
def teardown_db(exception):
    commands = g.pop("commands", None)

    if commands is not None:
        pass
        # write down commands


@click.command()
def start():
    os.environ["FLASK_APP"] = __file__
    subprocess.run(["flask", "run"])


if __name__ == "__main__":
    logger.info("starting umm server")
    start()
