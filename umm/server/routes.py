from umm.server.utils import get_commands

commands = get_commands()


def available_tags(request):
    return commands.tags_dict


def available_commands(request):
    return commands.command_dict


def request_command(request):
    # get command
    return {"command": []}


def confirm_command(request):
    # increment the number
    return {"recieved": True}
