from os import environ
from flask import jsonify, request

import requests

from datetime import datetime

#e.g.  https://api.darksky.net/forecast/977906b441a7d686a742e98e52a3acd4/37.8267,-122.4233
class Forecast:

  #What other weather info do we need?
  def __init__(self, info):

    self.forecast = info['summary']
    epoch_seconds = int(info['time'])
    self.time = datetime.utcfromtimestamp(
        epoch_seconds).strftime("%A %B %d, %Y")    

  def serialize(self):
    return vars(self)

  @staticmethod
  def fetch(lat, long):
    """
    INPUT (latitude, longitude)
    returns JSON string with search_query, formatted_query, and weather information
    """

    api_key = environ.get('WEATHER_API_KEY')
    
    url = f"https://api.darksky.net/forecast/{api_key}/{lat},{long}"

    forecasts = requests.get(url).json()

    dailies = [Forecast(daily).serialize()
                for daily in forecasts['daily']['data']]

    return jsonify(dailies)