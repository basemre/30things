import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'your_api_key'}

connection.request('GET', '/v2/competitions/', None, headers )
response = json.loads(connection.getresponse().read().decode())

with open(response) as f:
    data=json.load(f)

print (data)