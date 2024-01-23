#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """ GET /
    Return:
      - Welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")