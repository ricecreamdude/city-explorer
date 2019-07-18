from Flask import jsonify
from os import environ

import requests


class Movie:
  def __init__(self, data):
    self.title = data['title']
    self.overview = data['overview']
    self.average_votes = data['vote_average']
    self.total_votes = data['vote_count']
    self.image_url = 'https://image.tmdb.org/t/p/w500' + data['poster_path']
    self.popularity = data['popularity']
    self.released_on = data['release_date']

  def serialize(self):
    return vars(self)

  @staticmethod
  def fetch(query):  


    api_key = environ.get('MOVIE_API_KEY')
    query = "Up"
    

    url = f'https://api.themoviedb.org/3/search/movie/?api_key={api_key}&language=en-US&page=1&query={query}'

    response = requests.get(url).json()

    


    return jsonify(response)
