import os
from datetime import timedelta

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    from miscellaneous.home.views import home_blueprint
    app.register_blueprint(home_blueprint)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0', port=7000)
