"""
    Sendet informationen an einem Webservice
"""

import json

TOKEN = 'some secret keys'
MANTIS_API = 'someurlto mantis bugtracker'
STANDORT = "ein standort"


def readConfig():
    global TOKEN, MANTIS_API, STANDORT
    
    content = open("config.json").read()
    config = json.loads(content)

    TOKEN = config['token']
    MANTIS_API = config['mantisapi']
    STANDORT = config['standort']


readConfig()
