from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask inside Docker!! - new revision"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host="0.0.0.0", port=port)
