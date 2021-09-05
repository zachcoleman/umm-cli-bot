from typing import List

from umm.server.command import Command


class CommandSet:
    def __init__(self, commands: List[Command]):

        tags_dict = {}
        for c in commands:
            for tag in c.tags:
                if tag in tags_dict:
                    tags_dict[tag].append(c.id)
                else:
                    tags_dict[tag] = [c.id]

        self.command_dict = {c.id: c for c in commands}
        self.tags_dict = tags_dict

    def get_candidates(tokens: List[str]):
        pass
