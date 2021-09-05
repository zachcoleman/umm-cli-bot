import json
from functools import partial

from aiohttp import web

from umm.server.utils import get_commands

commands = get_commands()


async def available_tags(request):
    resp_json = commands.tags_dict
    _ = list(request.query.keys())
    return web.json_response(resp_json, dumps=partial(json.dumps, indent=2))


async def available_commands(request):
    resp_json = commands.command_dict
    return web.json_response(
        resp_json, dumps=partial(json.dumps, default=vars, indent=2)
    )


async def request_command(request):
    resp_json = {"command": []}
    return web.json_response(resp_json, dumps=partial(json.dumps, indent=2))


async def confirm_command(request):
    resp_json = {"recieved": True}
    return web.json_response(resp_json, dumps=partial(json.dumps, indent=2))
