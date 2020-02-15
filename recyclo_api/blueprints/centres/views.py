from flask import Blueprint, jsonify, request
from models.centre import Centre
import requests
import os

centres_blueprint = Blueprint('centres',
                                __name__,
                                template_folder='templates')

#parse in next academy
@centres_blueprint.route('/',methods=['GET'])
def index():
    # breakpoint()
    # current_location = {"lat":3.134873,"lng":101.6299415}
    # current_location = request.get_json().get('lat') and request.get_json().get('lng')
    current_location = request.get_json()
    if not current_location:
        return jsonify({'message' : 'please parse "lat" & "lng" coordinates'}), 418

    centres = Centre.select()
    distance_list = []
    for centre in centres:
        get_distance = requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={current_location["lat"]},{current_location["lng"]}&destinations=place_id:{centre.place_id}&key={os.environ.get("GOOGLE_MAP_API")}')

        x = get_distance.json()['rows'][0]['elements'][0]
        obj = {
            'name':centre.name,
            'distance': x['distance']['text'],
            'place_id' : centre.place_id
        }
        distance_list.append(obj)

    sorted_list = sorted(distance_list, key = lambda i: (['distance'))

    return jsonify({
            'centres' : sorted_list
    }), 200









    #get all centres

    # centres = Centre.select()
    # return jsonify([{
    #     'id' : centre.id,
    #     'name' : centre.name,
    #     'place_id' : centre.place_id
    # } for centre in centres
    # ])



    # ipc = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=IPC%20Recycling%20&%20Buy-Back%20Centre&inputtype=textquery&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBn7jYGlUVP-bN2rXnr2gQDy2ZxzKOcgvk')
    # kayu = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Tzu%20Chi%20Kayu%20Ara%20Recycle%20Center&inputtype=textquery&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBn7jYGlUVP-bN2rXnr2gQDy2ZxzKOcgvk')
    # tzuchi = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Tzu%20Chi%20Recycling%20Point&inputtype=textquery&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBn7jYGlUVP-bN2rXnr2gQDy2ZxzKOcgvk')
    # nextaca = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=NEXT%20Academy&inputtype=textquery&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBn7jYGlUVP-bN2rXnr2gQDy2ZxzKOcgvk')
    # coor = ipc.json()['candidates'][0]['geometry']['location']
    # print(coor['lat'],coor['lng'])
    # obj = {
    #     'lat' :coor['lat'],
    #     'lng' :coor['lng']
    # }
    # coor = [ipc.json(), kayu.json(), tzuchi.json(), nextaca.json()]
    # return jsonify(coor)

    # next_place_id = ChIJh819ADlJzDERuOXOhQOZCB8

    # next_academy_place_id = 

#hardcode place_id to centre table
#user will parse in their location (lat & lng) when click, server shall return closest centre with name, place_id, & distance.
#user will select desired centre and app will run googleMap with inputs all parsed.


# user input location name
# returns input's place_id
# returns distance between user's place_id and centre's place_id


# user chooses a centre
# runs google MAP api, with origin and destination place id attached.

