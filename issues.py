"""
    Sendet informationen an einem Webservice
"""

import requests
import config
import json


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
    authHeaders = {"Authorization": config.TOKEN, "Content-Type": "application/json"}
    
    print('------------------------------------------------------------------')
    print(json.dumps(issueJson, indent=4))
    print('------------------------------------------------------------------')
    
    weiter = input('Soll der Mantis Eintrag erzeugt werden? (y,n)? ')
    
    if weiter == 'y':
        print("Versuche Mantis-Eintrag zu erzeugen: " + config.MANTIS_API)
        
        result = requests.post(url, json = issueJson, headers = authHeaders)
        resultJson = json.loads(str(result.content.decode()))
        issueId = str(resultJson['issue']['id'])
        
        print("Eintrag erstellt: " + issueId)

