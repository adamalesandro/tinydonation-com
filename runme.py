import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.context_processor
def inject_values():
    return {
        "kickstarter_url": "https://www.kickstarter.com/projects/2118183266/tinydonation-encouraging-micro-donations-using-tec"
    }


if __name__ == "__main__":
    app.run("localhost", port=8888)