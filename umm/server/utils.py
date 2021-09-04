import yaml
from flask import g

from umm.server.command import Command, CommandSet


def get_commands():
    if "commands" not in g:
        g.commands = parse_commands("../ resources/commands.yaml")
    return g.commands


def parse_commands(path: str):
    """"""
    with open(path) as f:
        comm_dict = yaml.full_load(f)
    commands = []
    for k, v in comm_dict["commands"].items():
        commands.append(Command(id=k, command=v["command"], tags=v["tags"]))

    return CommandSet(commands)
