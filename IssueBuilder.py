'''
  Diese Klasse unterstützt beim erzeugen der Daten für Mantis
'''

import json
import subprocess
import config
import readhw

def summary(lshwJson):
    return lshwJson['vendor'] + " " + lshwJson['product']

def category(lshwJson):
    if lshwJson["configuration"]["chassis"] == 'notebook':
        return "Notebook"
    else:
        return "Desktop"
    
def build():
    
    lshwRaw = subprocess.check_output("sudo -S lshw -json", shell=True, universal_newlines=True)
    lshwJson = json.loads(str(lshwRaw))[0]
    
    custom_fields = [
        {"field": {"name": "cpu"}, "value": readhw.cpu()},
        {"field": {"name": "Ram"}, "value": readhw.memory()},
        {"field": {"name": "eingang"}, "value": ""}, # heute
        {"field": {"name": "Festplatte"}, "value": ""}, # größe und typ
        {"field": {"name": "webcam"}, "value": ""}, # irgendwie testen ob erkannt und geht
        {"field": {"name": "wlan"}, "value": ""}, # irgendwie testen ob erkannt und geht
        {"field": {"name": "Standort"}, "value": config.STANDORT} 
    ]
    
    description = ""
    
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
                
    