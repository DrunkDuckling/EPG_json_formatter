import json
import requests
import Constants
# Might not need Just if an API Key is needed for the request Example: HTTPBasicAuth('apikey', '1234abcd')
# Get key from constants file. 
from requests.auth import HTTPBasicAuth

# Opens a json file contaning the data needed to be send.
# And makes it into a dictonary
print('Opening Json file contaning Data.. ')
d = open('data.json')
data = json.load(d)
d.close()

# URL, and headers for the API End point
URL = Constants.API_ENDPOINT
headers = { 'content-type' : 'application/json'}

# Request AWS with a post using the URL, headers and the EPG data
# Response comes in the txt format so can be read with .text
print('Making request to the Web-Service.. ') 
response = requests.post(URL, headers=headers, data=json.dumps(data))
print('Response: ' + str(response.status_code) + '\n')
# Print the response so the user can see it. 
print('-------------------------------------------------------------')
print(response.text)
print('-------------------------------------------------------------' + '\n')


# Creates a txt file contaning the response from the server so the user does not need to use the console to read output
print('Generating file with response in execution folder..')
with open('response.txt', 'w') as f:
    f.write(response.text)
print('File generated Sucessfully.')
