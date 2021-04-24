from flask import Flask, render_template, session, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import re
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import folium
from flask import jsonify
from flask_simple_geoip import SimpleGeoIP

app = Flask(__name__, template_folder = 'templates')

#Custom User types
class User:
    def __init__(self, name, lat, lng):
        self.name=name
        self.lat=lat
        self.lng=lng

users=(
    User('Shreyas',37.9045286, -122.1445772),
    User('Vidhi',37.8884474, -122.1155922),
    User('Regina',37.7884474, -122.0155922)
)


@app.route("/map-marker")
def map_marker():
    # this map using stamen terrain
    lat_list=[]
    lng_list=[]
    name_list=[]

    for user in users:
        lat_list.append(user.lat)
        lng_list.append(user.lng)
        name_list.append(user.name)


    map = folium.Map(
        location=[lat_list[0], lng_list[0]],
        tiles='Stamen Terrain',
        zoom_start=12
    )

    folium.Marker(
        location=[lat_list[1], lng_list[1]],
        popup="<b>Vidhi here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='white')
    ).add_to(map)

    folium.Marker(
        location=[lat_list[2], lng_list[2]],
        popup="<b> Shreyas here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='green')
    ).add_to(map)

    folium.Marker(
        location=[45.53236, -122.8750],
        popup="<b>Marker 3 here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='red')
    ).add_to(map)

    return map._repr_html_()


app.config["GEOIPIFY_API_KEY"] = "at_LXAL8yAaI4niLHwdKoX9k9zD3G4O1"

simple_geoip = SimpleGeoIP(app)

@app.route("/getLocation")
def test():
    geoip_data = simple_geoip.get_geoip_data()
    return jsonify(data=geoip_data)


if __name__ == "__main__":
    app.run(debug=True)