from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# register blueprints
# app.register_blueprint(mod)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


db.create_all()
