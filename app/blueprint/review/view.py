import requests
from app.database import db
from time import gmtime, strftime
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
    name = request.form['user_name']

    current_time = strftime("%m-%d-%Y %H:%M", gmtime())

    business = Business(
        business_id=id,
        comment_user=name,
        comment_rating=rating,
        comment_content=reason,
        comment_time=current_time
    )
    db.session.add(business)
    db.session.commit()

    url = '/detail/' + id

    return redirect(url, code=302)


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.String(100), nullable=False)
    comment_user = db.Column(db.String(200))
    comment_rating = db.Column(db.Integer)
    comment_content = db.Column(db.Text)
    comment_time = db.Column(db.String(100))
