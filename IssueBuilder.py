'''
  Diese Klasse unterstützt beim erzeugen der Daten für Mantis
'''

import json
import subprocess
import config
import readhw
from datetime import datetime
import base64


def summary(lshwJson):
    return lshwJson['vendor'] + " " + lshwJson['product']


def category(lshwJson):
    if lshwJson.get("configuration").get("chassis") == 'notebook' or lshwJson.get("configuration").get(
            "chassis") == 'laptop':
        return "Notebook"
    else:
        return "Desktop"


def os():
    return subprocess.check_output("grep -i PRETTY_NAME -s -d skip /etc/*-release | awk -F'=' '{ print $2 }'",
                                   shell=True, universal_newlines=True).strip().replace('\"', '')


def build():
    print("Sammle Informationen über den Computer...")
    lshwRaw = subprocess.check_output("sudo -S lshw -json -quiet", shell=True, universal_newlines=True)
    lshwJson = json.loads(str(lshwRaw))[0]

    custom_fields = [
        {"field": {"name": "cpu"}, "value": readhw.cpu()},
        {"field": {"name": "Ram"}, "value": readhw.memory()},
        {"field": {"name": "eingang"}, "value": datetime.now().timestamp()},
        {"field": {"name": "Festplatte"}, "value": readhw.storage()},  # größe und typ
        {"field": {"name": "webcam"}, "value": readhw.check_for_cam()},
        {"field": {"name": "wlan"}, "value": readhw.wifi()},  # irgendwie testen ob erkannt und geht
        {"field": {"name": "Standort"}, "value": config.STANDORT}
    ]

    print(
        "Jetzt darfst du weitere Informationen eingeben die du der Description hinzufügen möchtest. z.B. Besonderheiten des Computers: Farbe, krasses Display, Beschädigungen oder Defekte, etc. Um zu beenden gib Fertig ein.")
    more_description_input = ['\t']

    while True:
        line = input()
        if line != "Fertig":
            more_description_input.append(line)
        else:
            break

    more_description_input = '\n            '.join(more_description_input)

    print("Sammle weitere Informationen...")
    description = "USB 3: " + readhw.usb3() + "\n" \
                                              "Grafikkarte: " + readhw.graphicscard() + "\n" \
                                                                                        "Sonstiges: " + more_description_input

    print(description)

    hardwareAttachment = base64.b64encode(subprocess.check_output("sudo lshw -short -quiet", shell=True)).decode()

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