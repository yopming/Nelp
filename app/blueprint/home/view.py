import json
import requests
from flask import Blueprint, render_template, redirect, url_for, request

blueprint_home = Blueprint('home', __name__, template_folder='templates')

@blueprint_home.route('/')
def home_show():
    return render_template('index.html')


@blueprint_home.route('/list')
def home_query():
    path_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    path_location = "location=33.993039,-81.0305768"
    path_radius = "&radius=50000"
    path_type = "&type=restaurant"
    path_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
    key_word = "&keyword=" + request.args.get('keyword')
    path = path_base + path_location + path_radius + path_type +key_word+ path_key
    try:
        responseData = requests.post(path)
    except requests.ConnectionError:
        print ('Connection Error')
    Jresponse = responseData.text
    data = json.loads(Jresponse)
    results = data['results']
    next_token = data['next_page_token']
    idlist = []
    namelist = []
    iconlist = []
    placeidlist = []
    addresslist = []
    photolist = []
    for result in results:
        idlist.append(result['id'])
        placeidlist.append(result['place_id'])
        namelist.append(result['name'])
        iconlist.append(result['icon'])
        addresslist.append(result['vicinity'])

        if 'photos' in result:
            if result['photos'][0]['photo_reference']:
                path_photo_base = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
                path_photo_reference = result['photos'][0]['photo_reference']
                path_photo_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
                path_photo = path_photo_base + path_photo_reference + path_photo_key
                photolist.append(path_photo)

    return render_template('list.html',
                           id_list=idlist,
                           placeid_list=placeidlist,
                           name_list=namelist,
                           icon_list=iconlist,
                           address_list=addresslist,
                           photo_list=photolist
                           )

