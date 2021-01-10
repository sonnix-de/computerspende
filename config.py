"""
    Sendet informationen an einem Webservice
"""

import json, os


def createConfigFile():
    config = {}
    print("Es wird nun eine Konfigurationsdatei config.json erstellt.")
    config['token'] = input("Gib den Token ein:")
    config['standort'] = input("Gib den Standort ein:")
    config['mantisapi'] = "https://assets.computerspende-regensburg.de/rest/api/"
    with open ('config.json', 'a+') as file:
        json.dump(config, file)


def readConfig():
    global TOKEN, MANTIS_API, STANDORT
    if not os.path.exists('config.json'):
        createConfigFile()
    content = open("config.json").read()
    config = json.loads(content)

    TOKEN = config['token']
    MANTIS_API = config['mantisapi']
    STANDORT = config['standort']


readConfig()
