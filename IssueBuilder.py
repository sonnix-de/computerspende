'''
  Diese Klasse unterstützt beim erzeugen der Daten für Mantis
'''

import json
import subprocess
import readhw
from datetime import datetime
import base64

def summary(lshwJson):
    return lshwJson['vendor'] + " " + lshwJson['product']


def category(lshwJson):
    if lshwJson.get("configuration").get("chassis") == 'notebook' or lshwJson.get("configuration").get("chassis") == 'laptop':
        return "Notebook"
    else:
        return "Desktop"


def os():
    return subprocess.check_output("grep -i PRETTY_NAME -s -d skip /etc/*-release | awk -F'=' '{ print $2 }'", shell=True, universal_newlines=True).strip().replace('\"', '')
    

def build():
    
    lshwRaw = subprocess.check_output("sudo -S lshw -json", shell=True, universal_newlines=True)
    lshwJson = json.loads(str(lshwRaw))[0]

    content = open("config.json").read()
    config = json.loads(content)
    STANDORT = config['standort']

    custom_fields = [
        {"field": {"name": "cpu"}, "value": readhw.cpu()},
        {"field": {"name": "Ram"}, "value": readhw.memory()},
        {"field": {"name": "eingang"}, "value": datetime.now().timestamp()},
        {"field": {"name": "Festplatte"}, "value": readhw.storage()},  # größe und typ
        {"field": {"name": "webcam"}, "value": readhw.check_for_cam()},
        {"field": {"name": "wlan"}, "value": readhw.wifi()},  # irgendwie testen ob erkannt und geht
        {"field": {"name": "Standort"}, "value": STANDORT},
        {"field": {"name": "Betriebssystem"}, "value": readhw.osversion()}
    ]
    
    print("Jetzt darfst du weitere Informationen eingeben die du der Description hinzufügen möchtest. z.B. Besonderheiten des Computers: Farbe, krasses Display, Beschädigungen oder Defekte, etc. Wenn du Fertig bist drücke CTRL+D")
    more_description_input = []
    while True:
        try:
            line = input()
            more_description_input.append(line)
        except EOFError:
            break

    description = "USB 3: " + readhw.usb3() + "\n" \
                  "Grafikkarte: " + readhw.graphicscard() + "\n" \
                  "Auflösung: " + readhw.resolution() + "\n" \
                  "Sonstiges: " + '\n\t    '.join(map(str, more_description_input))

    print(description)
    
    hardwareAttachment = base64.b64encode(subprocess.check_output("sudo lshw -short", shell=True)).decode()
    
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
        },
        "files": [
            {
                "name": "lshw_output.txt",
                "content": hardwareAttachment                
            }
        ]
    }
    print(mantisJson)
    return mantisJson


# print(build())