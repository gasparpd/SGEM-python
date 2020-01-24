from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route("/saluda/<nombre>")
def hello(nombre):
    return jsonify("Hello {}!".format(nombre))


if __name__ == "__main__":
    app.run()