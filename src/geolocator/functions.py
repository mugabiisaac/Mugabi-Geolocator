import urllib2
import json
import time

from geopy import geocoders

#from .apis import *


def find_city_lat_lng(lat, lng):
    g = geocoders.GoogleV3()
    find = "%s %s" % (lat, lng)
    location = g.geocode(find)
    address = location.raw['address_components']
    city_names = [component['long_name']
                 for component in address
                 if 'locality' in component['types']]
    return city_names[0]

'''
def locu_search(query):
	#api = LOCU_API

	url = 'https://api.locu.com/v1_0/venue/search/?'

	local = query

	locality = local.replace(' ', '%20')

	new_url = url + 'api_key=' + api + '&locality=' + locality

	obj = urllib2.urlopen(new_url)

	data = json.load(obj)

	locations = [[abc['name'], abc['id']] for abc in data['objects']]

	return locations


def locu_details(locu_id):
    api = LOCU_API

    url = 'https://api.locu.com/v1_0/venue/'

    new_url = url + locu_id + '/?api_key=' + api

    obj = urllib2.urlopen(new_url)

    data = json.load(obj)

    for abc in data['objects']:
        details = [abc['lat'], abc['long']]   # Assume only one object returned

    return details
'''


def find_place(query):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(query)
    return place, lat, lng


def foursquare_search(query):
    token = FOURSQUARE_TOKEN

    today = time.strftime("%Y%m%d")

    place, lat, lng = find_place(query)

    latlng = str(lat) + '%2C%20' + str(lng)

    url = 'https://api.foursquare.com/v2/venues/search?intent=checkin'

    full_url = url + '&v=' + today + '&ll=' + latlng + '&oauth_token=' + token

    obj = urllib2.urlopen(full_url)

    data = json.load(obj)

    locations = [[abc['name'], abc['id']] for abc in data['response']['venues']]

    # for abc in data['response']['venues']:
    #     print abc['name']
    #     try:
    #         print 'phone   = ' + abc['contact']['phone']
    #     except Exception:
    #         pass
    #     try:
    #         print 'twitter = ' + abc['contact']['twitter']
    #     except Exception:
    #         pass
    #     try:
    #         print 'city    = ' + abc['location']['city']
    #     except Exception:
    #         pass

    return locations


def foursquare_details(four_id):
    token = FOURSQUARE_TOKEN

    today = time.strftime("%Y%m%d")

    url = 'https://api.foursquare.com/v2/venues/'

    full_url = url + four_id + '?v=' + today + '&oauth_token=' + token

    obj = urllib2.urlopen(full_url)

    data = json.load(obj)

    venue = data['response']['venue']

    details = [venue['location']['lat'], venue['location']['lng']]

    return details
