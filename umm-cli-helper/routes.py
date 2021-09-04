from __main__ import app
from flask import g


@app.route("/tags")
def tags():
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
