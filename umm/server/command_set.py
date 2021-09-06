import os
from typing import List

import yaml

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

    def get_candidates(self, tags: List[str]):
        candidates = {}
        for tag in tags:
            command_ids = self.tags_dict.get(tag, [])
            for id in command_ids:
                candidates[id] = candidates.get(id, 0) + 1

        candidates_sorted = sorted(
            [
                (tag_count, self.command_dict[id].freq, id)
                for id, tag_count in candidates.items()
            ],
            reverse=True,
        )

        return [self.command_dict[id] for _, _, id in candidates_sorted]

    def increment_freq(self, id: str):
        self.command_dict[id].freq += 1

    def write_down(self):
        dir_name = os.path.dirname(__file__)
        tmp_file_name = os.path.join(dir_name, "../resources/tmp_commands.yaml")
        file_name = os.path.join(dir_name, "../resources/commands.yaml")

        serialize_dict = dict(
            commands={id: c.__dict__ for id, c in self.command_dict.items()}
        )

        with open(tmp_file_name, "w") as f:
            yaml.dump(serialize_dict, f)

        if os.path.exists(file_name):
            os.remove(file_name)
        os.rename(tmp_file_name, file_name)
