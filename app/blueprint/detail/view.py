import requests
from flask import Blueprint, render_template

blueprint_detail = Blueprint('detail', __name__, template_folder='templates')

@blueprint_detail.route('/<id>')
def show_detail(id):
    # get details from google
    path_base = "https://maps.googleapis.com/maps/api/place/details/json?"
    path_place_prefix = "placeid="
    path_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
    path = path_base + path_place_prefix + id + path_key

    r = requests.get(path)
    data = r.json()

    data_result = data['result']
    business_name = data_result['name']
    business_address = data_result['formatted_address']
    business_phone_number = data_result['formatted_phone_number']

    if 'photos' in data_result:
        path_photo_base = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
        path_photo_reference = data_result['photos'][0]['photo_reference']
        path_photo_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
        path_photo = path_photo_base + path_photo_reference + path_photo_key


    # get comments from database

    return render_template('detail.html',
                           name = business_name,
                           address = business_address,
                           number = business_phone_number,
                           photo = path_photo,
                           id = id
                           )
