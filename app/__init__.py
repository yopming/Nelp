from flask import Flask, render_template
from app.database import db
from app.blueprint.home.view import blueprint_home
from app.blueprint.list.view import blueprint_list
from app.blueprint.detail.view import blueprint_detail
from app.blueprint.review.view import blueprint_review

import config

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# register blueprints
app.register_blueprint(blueprint_home)
app.register_blueprint(blueprint_list, url_prefix='/list')
app.register_blueprint(blueprint_detail, url_prefix='/detail')
app.register_blueprint(blueprint_review, url_prefix='/review')

db.init_app(app)
