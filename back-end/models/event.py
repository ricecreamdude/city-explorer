from flask import jsonify, request
from os import environ

import requests

class Event:
  def __init__(self, data):
    self.name = data['name']['text']
    self.url = data['url']
    self.created = data['created']
    self.summary = data['summary']


  def serialize(self):
    return vars(self)

  @staticmethod
  def fetch(location):

    api_key = environ.get('EVENTBRITE_API_KEY')

    url = f'https://www.eventbriteapi.com/v3/events/search?token={api_key}&location.address={location}'

    response = requests.get(url).json()

    eventsList = [ Event(event).serialize() for event in response["events"] ]

    return jsonify(eventsList)