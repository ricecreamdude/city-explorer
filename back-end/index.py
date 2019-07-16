from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

import os
import json
import requests


PORT = 3000

#Build handler for HTTP Get Request
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):

    ##Detects url path
    parsed_path = urlparse(self.path)
    print('request path', parsed_path.path)

    ##parses query
    parsed_qs = parse_qs(parsed_path.query)
    print('parsed query', parsed_qs)

    if parsed_path.path == '/locations':
      
      #Basic HTTP request info
      self.send_response(200)      
      self.send_header('Content-type', 'application/json')
      self.end_headers()

      query = parsed_qs['place']
      api_key = 'AIzaSyCz4_13_FImCJdgbqeWYrglhmkcBRW5mgg'    

      # http://localhost:3000/weather?data[latitude]=41.3850639&data[longitude]=2.1734035

      #Construct our query
      url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'

      # print('url', url)

      #Parse incoming data string into python or json
      result = requests.get(url).json()
      print('results!!!!', result['results'][0]['geometry']['location'])
      


      ##Create a new class and push it to the page
      
      #Print JSON onto page using wfile.write
      json_string = json.dumps(result)
      self.wfile.write(json_string.encode())
      
      # { 'formatted_query':'the place', 
      # 'search_query':'what they typed', 
      # 'latitude':100.0, 
      # 'longitude':100.0 }

      return

def create_server():
  return HTTPServer(
    ('127.0.0.1', PORT), SimpleHTTPRequestHandler
  )

def run_forever():
  server = create_server()

  try:
    print(f'Starting server on port {PORT}')
    server.serve_forever()
  except KeyboardInterrupt:
    server.server_close()
    server.shutdown()
    print('Server Closed')

if __name__ == "__main__":
    run_forever()
    handler = SimpleHTTPRequestHandler()

# { 'formatted_query':'the place', 
# 'search_query':'what they typed', 
# 'latitude':100.0, 
# 'longitude':100.0 }

class LocationQuery:

  def __init__(self,query,search,lat,long):
    self.formatted_query = query
    self.search_query = search
    self.latitude = lat
    self.longitude = long

  def serialize(self):
    return vars(self)
