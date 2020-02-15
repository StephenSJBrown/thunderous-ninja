from flask import Blueprint, jsonify, request
from models.centre import Centre
import requests
import os

centres_blueprint = Blueprint('centres',
                                __name__,
                                template_folder='templates')

#parse in next academy
@centres_blueprint.route('/', methods=['POST'])
def index():
    # breakpoint()
    # current_location = {"lat":3.134873,"lng":101.6299415}
    # current_location = request.get_json().get('lat') and request.get_json().get('lng')
    current_location = request.get_json()
    print(current_location)
    if not current_location:
        return jsonify({'message' : 'please parse "lat" & "lng" coordinates'}), 418

    centres = Centre.select()
    distance_list = []
    for centre in centres:
        get_distance = requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={current_location["lat"]},{current_location["lng"]}&destinations=place_id:{centre.place_id}&key={os.environ.get("GOOGLE_MAP_API")}')
        # breakpoint()
        centre_distance = get_distance.json()['rows'][0]['elements'][0]
        distance = centre_distance['distance']['text']
        floatify = float(distance.split(' ')[0])
        print(floatify)
        obj = {
            'name':centre.name,
            'distance': floatify,
            'place_id' : centre.place_id
        }
        distance_list.append(obj)

    sorted_list = sorted(distance_list, key = lambda i: i['distance'])

    return jsonify({
            'centres' : sorted_list
    }), 200









 
