#!/usr/bin/python3
"""The / home route with flask"""


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_route():
        """root route"""
        return "Hello HBNB!"

    app.run(host='0.0.0.0',port=5000)
