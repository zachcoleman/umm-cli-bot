from __main__ import app


@app.route("/help")
def index():
    # let's report on .yamls here
    return "<p>Hello, World!</p>"
