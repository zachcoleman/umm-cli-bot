import uuid
from typing import List


class Command:
    def __init__(
        self,
        command: List[str],
        tags: List[str],
        id: str = None,
        freq: int = None,
        prompts: List[str] = None,
    ):
        """"""
        assert len(command) > 0, "command length 0"
        assert len(tags) > 0, "tags length 0"
        self.command = command
        self.tags = tags
        self.id = id if id else uuid.uuid4()
        self.freq = freq if freq else 0
        self.prompts = prompts if prompts else []


class CommandSet:
    def __init__(self, commands: List[Command]):

        tag_dict = {}
        for c in commands:
            for tag in c.tags:
                if tag in tag_dict:
                    tag_dict[tag].append(c.id)
                else:
                    tag_dict[tag] = [c.id]

        self.command_dict = {c.id: c for c in commands}
        self.tag_dict = tag

    def get_candidates(tokens: List[str]):
        pass
