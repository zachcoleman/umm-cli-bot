from flask import g

from umm.server import app


@app.teardown_appcontext
def teardown_commands(exception):
    commands = g.pop("commands", None)
    if commands is not None:
        pass
        # write down commands


@app.route("/tags")
def tags():
    app.get_commands()
    return g.commands.tag_dict


@app.route("/commands")
def commands():
    return g.commands.command_dict


@app.route("/command")
def request_command():
    # get command
    return {"command": []}


@app.route("/confirm")
def confirm_command():
    # increment the number
    return {"recieved": True}
