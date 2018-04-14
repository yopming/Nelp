from flask import Blueprint, render_template

blueprint_list = Blueprint('list', __name__, template_folder='templates')
