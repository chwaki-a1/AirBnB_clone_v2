#!/usr/bin/python3
"""The / home route"""


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """root route"""
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb_route():
        """root hbnb route"""
        return "HBNB"

    app.run(host='0.0.0.0',port=5000)
