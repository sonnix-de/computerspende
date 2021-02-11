"""
    Sendet informationen an einem Webservice
"""

import json, os


def createConfigFile():
    config = {}
    print("Es wird nun eine Konfigurationsdatei config.json erstellt.")
    config['token'] = input("Gib deinen generierten Mantis API-Token ein: ")
    config['standort'] = input("Gib den Standort ein, der bei jedem Gerät automatisch gewählt werden soll: ")
    config['mantisapi'] = "https://assets.computerspende-regensburg.de/api/rest/"
    with open ('config.json', 'w+') as file:
        json.dump(config, file, indent=2)
    print("Konfigurationsdatei erfolgreich erstellt.")


def readConfig():
    global TOKEN, MANTIS_API, STANDORT
    if os.path.exists('config.json'):
        print("Es ist bereits eine Konfigurationsdatei vorhanden.")
        istvorhanden = input("Möchtest du eine neue erzeugen? (j/n): ")
        if istvorhanden == "j":
            createConfigFile()
        else:
            pass
    else:
        createConfigFile()
    content = open("config.json").read()
    config = json.loads(content)

    TOKEN = config['token']
    MANTIS_API = config['mantisapi']
    STANDORT = config['standort']


readConfig()
