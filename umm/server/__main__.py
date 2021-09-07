from aiohttp import web

from umm.server.routes import (
    add_command,
    available_commands,
    confirm_command,
    request_command,
)
from umm.utils.config import parse_config


def setup_routes(app: web.Application):
    app.router.add_get("/commands", available_commands)
    app.router.add_get("/add", add_command)
    app.router.add_get("/umm", request_command)
    app.router.add_get("/confirm", confirm_command)


def main():
    config = parse_config()
    app = web.Application()
    setup_routes(app)
    web.run_app(app, port=config.port)


if __name__ == "__main__":
    main()
