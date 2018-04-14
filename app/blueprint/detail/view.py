import json
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
    _business_photos = data_result['photos']
    business_photos = []
    photo_limit = 0
    for pho in _business_photos:
        url = pho['html_attributions'][0]
        business_photos.append(url)
        photo_limit += 1

        if photo_limit > 2:
            break

    # get comments from database

    return render_template('detail.html',
                           name = business_name,
                           address = business_address,
                           number = business_phone_number,
                           photos = business_photos
                           )
