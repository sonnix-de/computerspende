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
    if os.path.exists('config.json'):
        pass
        # print("Es ist bereits eine Konfigurationsdatei vorhanden.")
        # isavailable = input("Möchtest du eine neue erzeugen? (j/n): ")
        # if isavailable == "j":
        #     createConfigFile()
        # else:
        #     pass
    else:
        createConfigFile()