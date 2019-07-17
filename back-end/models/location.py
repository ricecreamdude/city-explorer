from os import environ
import json
import requests


class Location:

  def __init__(self, search_query, info):
    self.search_query = search_query
    self.formatted_query = info['formatted_address']
    self.latitude = info['geometry']['location']['lat']
    self.longitude = info['geometry']['location']['lng']

  def serialize(self):
    return vars(self)

  #The fancy method we'll use to call our data.   This means we'll need to fetch API key from this location
  @staticmethod
  def fetch(query):
    """
    Input [query] Fetches from location API
    returns serialized Python list with search_query, formatted_query, latitude, longitude
    """

    #fetch API key   
    api_key = environ.get('GEOCODE_API_KEY')
    
    #Construct URL
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'

    #fetch data via url
    locations = requests.get(url).json()

    #create a new class instance

    newLocation = Location(query, locations['results'][0])
    #return serialized version of the class instance
    #Return JSON object
    return json.dumps(newLocation.serialize())