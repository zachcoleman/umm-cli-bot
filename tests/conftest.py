import pytest
from aiohttp import web

from umm.server.__main__ import setup_routes
from umm.server.utils import setup_folder
from umm.utils.config import parse_config


@pytest.fixture
def commands(tmp_path):
    return setup_folder(root=tmp_path)


@pytest.fixture
def config(tmp_path):
    return parse_config(root=tmp_path)


@pytest.fixture
def app(commands, loop, aiohttp_client):
    app = web.Application()
    setup_routes(app, commands)
    return loop.run_until_complete(aiohttp_client(app))
