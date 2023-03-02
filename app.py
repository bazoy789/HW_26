from flask import Flask

from views import bp_pars
from db import db
from doc_config import Config


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(bp_pars)
    return app


app: Flask = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000, debug=True)
