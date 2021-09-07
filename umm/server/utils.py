import os

import yaml

from umm.server.command import Command
from umm.server.command_set import CommandSet


def parse_commands(path: str):
    """
    Args:
        path: string path to commands.yaml
    Returns:
        CommandSet built from commands.yaml file
    """
    with open(path) as f:
        comm_dict = yaml.full_load(f)
    commands = []
    for _, v in comm_dict["commands"].items():
        commands.append(Command(**v))

    return CommandSet(commands)


def get_commands():
    """
    Args:
        Nones
    Returns:
        CommandSet built from set resources path
    """
    dir_name = os.path.dirname(__file__)
    commands = parse_commands(os.path.join(dir_name, "../resources/commands.yaml"))
    return commands
