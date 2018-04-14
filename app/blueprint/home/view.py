import requests
import simplejson
import json
from flask import Blueprint, render_template, redirect, url_for
from app.blueprint.list.view import show_list

blueprint_home = Blueprint('home', __name__, template_folder='templates')

@blueprint_home.route('/')
def home_show():
    return render_template('index.html')


@blueprint_home.route('/api/query', methods=['POST'])
def home_query():
    path_base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    path_location = "location=33.993039,-81.0305768"
    path_radius = "&radius=50000"
    path_type = "&type=restaurant"
    path_key = "&key=AIzaSyDSBTpaBYPE4BQVmahrDrB974p3ysXjL0k"
    path = path_base + path_location + path_radius + path_type + path_key
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
    for result in results:
        idlist.append(result['id'])
        namelist.append(result['name'])
        iconlist.append(result['icon'])

    return render_template('list.html',
                           id_list = idlist,
                           name_list = namelist,
                           icon_list = iconlist
                           )

