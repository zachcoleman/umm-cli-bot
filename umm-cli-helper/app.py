import logging
import os
import subprocess
import sys

import click
from flask import Flask

logger = logging.getLogger(__file__)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
app = Flask(__name__)


@click.command()
def start():
    os.environ["FLASK_APP"] = __file__
    subprocess.run(["flask", "run"])


if __name__ == "__main__":
    logger.info("starting umm server")
    start()
