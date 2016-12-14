import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.context_processor
def inject_values():
    return {
        "kickstarter_url": "https://kickstarter.com/"
    }


if __name__ == "__main__":
    app.run("localhost", port=8888)