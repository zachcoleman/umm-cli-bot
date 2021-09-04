# noqa:  F401
from flask import Flask

import umm.server.routes
from umm.server.utils import get_commands

app = Flask(__name__)
get_commands()
