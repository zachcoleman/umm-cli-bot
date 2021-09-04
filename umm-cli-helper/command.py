import uuid
from typing import List


class Command:
    def __init__(
        self, command: List[str], tags: List[str], id: str = None, freq: int = None
    ):
        """"""
        assert len(command) > 0, "command length 0"
        assert len(tags) > 0, "tags length 0"
        self.command = command
        self.tags = tags
        self.id = id if id else uuid.uuid4()
        self.freq = freq if freq else 0
