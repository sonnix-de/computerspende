"""
    Sendet informationen an einem Webservice
"""

import requests
import json

TOKEN = 'some secret keys'
MANTIS_API = 'someurlto mantis bugtracker'

def readConfig():
    global TOKEN, MANTIS_API
    outfile = open("config.json")
    content = outfile.read()
    config = json.loads(content)
    TOKEN = config['token']
    MANTIS_API = config['mantisapi']

readConfig()
