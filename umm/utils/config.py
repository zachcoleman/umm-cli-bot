import os

import yaml
from pydantic import BaseModel

# TODO: switch to using pydantic for validating parsing


class Config(BaseModel):
    port: int


def parse_config():
    dir_name = os.path.dirname(__file__)
    with open(os.path.join(dir_name, "../resources/config.yaml")) as f:
        config = yaml.full_load(f)
    return Config.parse_obj(config)
