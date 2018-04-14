from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.blueprint.home.view import blueprint_home
from app.blueprint.list.view import blueprint_list
from app.blueprint.detail.view import blueprint_detail

import config

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# register blueprints
app.register_blueprint(blueprint_home)
app.register_blueprint(blueprint_list, url_prefix='/list')
app.register_blueprint(blueprint_detail, url_prefix='/detail')


db.create_all()
