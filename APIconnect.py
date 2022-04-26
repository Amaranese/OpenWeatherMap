import os


"""
API Key + Secret
If you're writing code for your own openweathermap account, enable an API key.
Next, create a Client object for interacting with the API:
API Key: blah
API Secret: blah
"""
directory = "../keys/weatherKEY.txt"
#initialize keys
api_key = ""
api_secret = ""

with open(directory, 'rU') as f:
    for line in f: # Iterate through rows
        keys = line.split(",")
        api_key = keys[0]
        api_secret = keys[1]


# Define global client
global URLconnection
URLkey = api_secret