"""
    Sendet informationen an einem Webservice
"""

import requests
import config as config


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


def createIssue(issueJson):

    url = config.MANTIS_API + 'issues/'
    authHeaders = {"Authorization": config.TOKEN,
               "Content-Type": "application/json"}
    print(issueJson)
    x = requests.post(url, json = issueJson, headers = authHeaders)
    print(x.text)


