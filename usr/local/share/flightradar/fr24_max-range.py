#!/usr/bin/python3

# Max range from geodesic aircraft distance (FR24)
# from localhost:8754/flights.json

from urllib.request import urlopen
import json
from math import *


def distance(lat1,lon1,lat2,lon2):

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    d = 2 * atan2(sqrt(a), sqrt(1 - a))

    return d

if __name__ == "__main__":

    R = 6373.0 / 1.852

    with open('/data/options.json', 'r') as f:
        options = json.load(f)
        if 'MLAT_EXACT_LAT' in options:
            ulat=radians(float( options['MLAT_EXACT_LAT'] ))
        else:
            ulat=float(0)
        if 'MLAT_EXACT_LON' in options:
            ulon=radians(float( options['MLAT_EXACT_LON'] ))
        else:
            ulon=float(0)

    url =  'http://localhost:8754/flights.json'

    with urlopen(url) as response:

        data = json.loads(response.read())

        dist = {}

        for key in data:
             icao=data[key][0]
             lat=data[key][1]
             lon=data[key][2]
             if (lat != 0.) and (lon != 0.):
                 lat=radians(float(lat))
                 lon=radians(float(lon))
                 dist[icao] = distance(ulat,ulon,lat,lon) * R

        sorted_dist=sorted(dist.items(), key=lambda x:x[1], reverse=True)

        if (sorted_dist and ulat != 0 and ulon != 0):
            sensor_mr = {"state": int(sorted_dist[0][1]),
                      "attributes": {"friendly_name": "Flightradar24 Max Range",
                      "icon": "mdi:map-marker-distance",
                      "state_class": "measurement",
                      "unit_of_measurement": "nm",
                      "unique_id": "fr24_max_range"} }
        else:
            sensor_mr = {"state": "0",
                      "attributes": {"friendly_name": "Flightradar24 Max Range",
                      "icon": "mdi:map-marker-distance",
                      "state_class": "measurement",
                      "unit_of_measurement": "nm",
                      "unique_id": "fr24_max_range"} }

        print(json.dumps(sensor_mr))
