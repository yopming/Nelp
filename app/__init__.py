from flask import Flask
from app.database import db
from app.blueprint.home.view import blueprint_home
from app.blueprint.list.view import blueprint_list
from app.blueprint.detail.view import blueprint_detail
from app.blueprint.review.view import blueprint_review

import config

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprints(app)
    register_extensions(app)

    return app

# register blueprints
def register_blueprints(app):
    app.register_blueprint(blueprint_home)
    app.register_blueprint(blueprint_list, url_prefix='/list')
    app.register_blueprint(blueprint_detail, url_prefix='/detail')
    app.register_blueprint(blueprint_review, url_prefix='/review')

def register_extensions(app):
    db.init_app(app)
