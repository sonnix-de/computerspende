"""
    Sendet informationen an einem Webservice
"""

import json, os


def createConfigFile():
    config = {}
    print("Es wird nun eine Konfigurationsdatei config.json erstellt.")
    config['token'] = input("Gib deinen generierten Mantis API-Token ein:")
    config['standort'] = input("Gib den Standort ein, der bei jedem Gerät automatisch gewählt werden soll:")
    config['mantisapi'] = "https://assets.computerspende-regensburg.de/api/rest/"
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
