import requests
from flask import Blueprint, render_template

blueprint_detail = Blueprint('detail', __name__, template_folder='templates')

@blueprint_detail.route('/<id>')
def show_detail(id):
    # get details from google

    # get comments from database

    return render_template('detail.html')
