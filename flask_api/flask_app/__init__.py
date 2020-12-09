from flask import Flask


def create_app():
    flask_app = Flask(__name__)

    @flask_app.route('/hello')
    def hello():
        return "Hello, it works!"

    return flask_app
