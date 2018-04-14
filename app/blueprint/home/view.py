from flask import Blueprint, render_template

blueprint_home = Blueprint('home', __name__, template_folder='templates')
@blueprint_home.route('/')
def show_home():
    return render_template('index.html')
