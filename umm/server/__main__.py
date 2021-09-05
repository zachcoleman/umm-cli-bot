from aiohttp import web

from umm.server.routes import (
    available_commands,
    available_tags,
    confirm_command,
    request_command,
)
from umm.utils.config import parse_config


def setup_routes(app):
    app.router.add_get("/tags", available_tags)
    app.router.add_get("/commands", available_commands)
    app.router.add_get("/umm", request_command)
    app.router.add_get("/confirm", confirm_command)


config = parse_config()
app = web.Application()
setup_routes(app)
web.run_app(app, port=config.port)
