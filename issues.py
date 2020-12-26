"""
    Sendet informationen an einem Webservice
"""

import requests
import json
import config as config
import helper as helper
import readhw as hw


def getIssueInfo(id):

    url = config.MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": config.TOKEN}
    x = requests.get(url, headers=headers)
    return x.json()


def updateIssue(id, updateInfo):

    url = config.MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": config.TOKEN,
               "Content-Type": "application/json"}
    print(updateInfo)
    x = requests.patch(url, json=updateInfo, headers=headers)
    print(x)


def setIssueInfo():
    # auslesen der Hardwareinformationen
    CCI = hw.getInformationAboutCurrentComputer()

    # Zusemmensetzen der Beschreibung
    description = """
    # SystemInformationen

    System: {}
    Realease: {}
    Version: {}

    ## CPU

    Physical Cores: {}
    Total Cores: {}
    """
    description = description.format(
        CCI['SystemInfo']['System'],
        CCI['SystemInfo']['Release'],
        CCI['SystemInfo']['Version'],
        CCI['CPU']['Pysical Cores'],
        CCI['CPU']['Total cores']
    )

    # CpuInfo
    cpu = "Physische Cores: " + str(CCI['CPU']['Pysical Cores'])

    # und formulierung der Updatestruktur
    # custom_fields funktioniert noch nicht!
    custom_fields = {"field": {"name": "cpu"}, "value": cpu}

    updateInfo = {"description": description, "custom_fields": custom_fields}
    return updateInfo


# helper.loadJsonFile("update.json")
# updateStructure =
# 25 ist das Beispiels-Issue
infos = updateIssue(25, setIssueInfo())
print(infos)
infos = getIssueInfo(25)
print(infos)

# updateInfo = str(updateInfo)
