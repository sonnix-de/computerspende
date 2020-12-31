'''
  Diese Klasse unterstützt beim erzeugen der Daten für Mantis
'''

import json
import subprocess
import config
import readhw
from datetime import datetime
import cv2


def summary(lshwJson):
    return lshwJson['vendor'] + " " + lshwJson['product']


def category(lshwJson):
    if lshwJson["configuration"]["chassis"] == 'notebook':
        return "Notebook"
    else:
        return "Desktop"


def check_for_cam(cam=0):
    cap = cv2.VideoCapture(cam)
    if cap is None or not cap.isOpened():
        return "Nein"
    else:
        return "Ja"


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
        "category": { 
            "name": category(lshwJson) 
        },
        "project": { 
            "name": "Computerliste" 
        }
    }
    return mantisJson


print(build())