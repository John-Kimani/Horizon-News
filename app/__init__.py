from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
import logging


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)


if not app.debug and not app.testing:
     if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)


from app import routes, errors