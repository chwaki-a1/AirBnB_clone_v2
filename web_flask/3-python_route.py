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
        """/hbnb/ route"""
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def c_route(text):
        """output some text after /c/"""
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def python_route(text):
        """output some text  after /python/"""
        return "Python " + text.replace('_', ' ')

    app.run(host='0.0.0.0', port=5000)
