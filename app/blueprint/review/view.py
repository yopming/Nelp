import requests
from flask import Blueprint, redirect, render_template, request

blueprint_review = Blueprint('review', __name__, template_folder='templates')


@blueprint_review.route('/<id>')
def review_show(id):
    path_base = "https://maps.googleapis.com/maps/api/place/details/json?"
    path_place_prefix = "placeid="
    path_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
    path = path_base + path_place_prefix + id + path_key

    r = requests.get(path)
    data = r.json()

    data_result = data['result']
    business_name = data_result['name']

    return render_template('review.html',
                           name=business_name,
                           id=id
                           )


@blueprint_review.route('/post', methods=['POST'])
def review_post():
    id = request.form['id']
    rating = request.form['rating']
    reason = request.form['reason']
    print(rating)
    print(reason)

    url = '/detail/' + id

    return redirect(url, code=302)
