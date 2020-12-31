'''
  Diese Klasse unterstützt beim erzeugen der Daten für Mantis
'''

import json
import subprocess
import config
import readhw
from datetime import datetime

def summary(lshwJson):
    return lshwJson['vendor'] + " " + lshwJson['product']


def category(lshwJson):
    if lshwJson["configuration"]["chassis"] == 'notebook':
        return "Notebook"
    else:
        return "Desktop"

def os():
    return subprocess.check_output("grep -i PRETTY_NAME -s -d skip /etc/*-release | awk -F'=' '{ print $2 }'", shell=True, universal_newlines=True).strip().replace('\"', '')
    

def build():
    
    lshwRaw = subprocess.check_output("sudo -S lshw -json", shell=True, universal_newlines=True)
    lshwJson = json.loads(str(lshwRaw))[0]
    
    custom_fields = [
        {"field": {"name": "cpu"}, "value": readhw.cpu()},
        {"field": {"name": "Ram"}, "value": readhw.memory()},
        {"field": {"name": "eingang"}, "value": datetime.now().timestamp()},
        {"field": {"name": "Festplatte"}, "value": readhw.storage()},  # größe und typ
        {"field": {"name": "webcam"}, "value": readhw.check_for_cam()},
        {"field": {"name": "wlan"}, "value": readhw.wif()},  # irgendwie testen ob erkannt und geht
        {"field": {"name": "Standort"}, "value": config.STANDORT} 
    ]
    
    description = "Some nice description" # TODO was machen wir in die description rein?
    
    mantisJson = {
        "summary": summary(lshwJson),
        "description": description, 
        "custom_fields": custom_fields,
        "os": os(),
        "category": { 
            "name": category(lshwJson) 
        },
        "project": { 
            "name": "Computerliste" 
        }
    }
    return mantisJson


print(build())