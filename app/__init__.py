from flask import Flask
from app.environment import Environment
from app.blueprints.twilio import twilio

def create_app(config_class=Environment):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(twilio, url_prefix='/twilio')

    return app