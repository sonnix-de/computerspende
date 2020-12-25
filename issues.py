"""
    Sendet informationen an einem Webservice
"""

import requests
import json
import config as config

def getIssueInfo(id):

    url = config.MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": config.TOKEN}
    x = requests.get(url, headers=headers)
    return x.json()

def updateIssue(id,update):
    url = config.MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": config.TOKEN}

infos = getIssueInfo(25)
print(infos)
