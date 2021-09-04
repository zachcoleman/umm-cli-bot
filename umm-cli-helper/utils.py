import yaml
from command import Command


def parse_commands(path: str):
    """"""
    with open(path) as f:
        comm_dict = yaml.full_load(f)
    commands = []
    for k, v in comm_dict["commands"].items():
        commands.append(Command(id=k, command=v["command"], tags=v["tags"]))

    return commands


if __name__ == "__main__":
    tmp = parse_commands("resources/commands.yaml")
    breakpoint()
