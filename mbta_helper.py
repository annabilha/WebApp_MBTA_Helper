import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)

MBTA_API_KEY = 'b27c9f30faed40b3b5f0bdd571efec4e'
MAPQUEST_API_KEY = 'rAMsEW4pLyT7KJ81DBWOObCMbA77JM0S'




# A little bit of scaffolding if you want to use it


def get_json(url):

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# ------
def get_lat_long(location):

    url = '{}?key={}&location={}'.format(MAPQUEST_BASE_URL, MAPQUEST_API_KEY, location)
    response = get_json(url)
    lat = response['results'][0]['locations'][0]['latLng']['lat']
    lng = response['results'][0]['locations'][0]['latLng']['lng']
    return lat,  lng

# -------
def get_nearest_station(lat, lng):
    # latitude, longitude = get_lat_long()
    url = '{}?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_BASE_URL,MBTA_API_KEY,lat,lng)
    print(url)
    response=get_json(url)
    stop_name = response ['data'][0]['attributes']['name']
    WC_accessible = response['data'][0]['attributes']['wheelchair_boarding']
    return stop_name, WC_accessible

# -----
def find_stop_near(location):
    lat, lng = get_lat_long(location)
    stop_name, WC_accessible = get_nearest_station(lat,lng)
    return stop_name, WC_accessible





# location= input("Insert Your Location")
# print(find_stop_near(location))
#
#
# if WC_accessible==0:
#          print(stop_name,"Not accessible to wheelchairs")
# else:
#          print(stop_name, "Accessible to wheelchair")
#
#
# def main():
#     """
#     You can all the functions here
#     """
#     pass
#
#
# if __name__ == '__main__':
#     main()