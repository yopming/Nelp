from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
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


# database
db = SQLAlchemy(app)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.String(100), nullable=False)
    comment_user = db.Column(db.String(200))
    comment_content = db.Column(db.Text)
    comment_time = db.Column(db.String(100))

db.create_all()


