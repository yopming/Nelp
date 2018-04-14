from flask import Blueprint, render_template

blueprint_list = Blueprint('list', __name__, template_folder='templates')

@blueprint_list.route('/')
def show_detail():
    return render_template('list.html')
