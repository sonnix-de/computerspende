"""
    Sendet informationen an einem Webservice
"""
from datetime import datetime

import requests, json

content = open("config.json").read()
config = json.loads(content)
TOKEN = config['token']
MANTIS_API = config['mantisapi']

def getIssueInfo(id):

    url = MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": TOKEN}
    x = requests.get(url, headers=headers)
    return x.json()


def updateIssue(id, updateInfo):

    url = MANTIS_API + 'issues/' + str(id)
    headers = {"Authorization": TOKEN,
               "Content-Type": "application/json"}
    print(updateInfo)
    x = requests.patch(url, json=updateInfo, headers=headers)
    print(x)


def createIssue(issueJson):

    url = MANTIS_API + 'issues/'
    authHeaders = {"Authorization": TOKEN, "Content-Type": "application/json"}

    print("\nDie folgenden Information konten gesammelt werden:" + "\n" +
        "Computerbeschreibung: " + str(issueJson['summary']) + "\n" +
        "CPU: " + str(issueJson["custom_fields"][0]['value']) + "\n" +
        "RAM: " + str(issueJson["custom_fields"][1]['value']) + "\n" +
        "Eingang: " + str(datetime.fromtimestamp(float(issueJson["custom_fields"][2]['value'])).strftime("%m/%d/%Y, %H:%M:%S")) + "\n" +
        "Festplatte: " + str(issueJson["custom_fields"][3]['value']) + "\n" +
        "Webcam: " + str(issueJson["custom_fields"][4]['value']) + "\n" +
        "WLAN: " + str(issueJson["custom_fields"][5]['value']) + "\n" +
        "Standort: " + str(issueJson["custom_fields"][6]['value']) + "\n" +
        "Description: " + str(issueJson['description']) + "\n" +
        "OS: " + str(issueJson['os']) + "\n" +
        "Category: " + str(issueJson['category']['name'])
        )
    
    weiter = input('Soll der Mantis Eintrag erzeugt werden? (y,n)? ')
    
    if weiter == 'y':
        print("Versuche Mantis-Eintrag zu erzeugen: " + MANTIS_API)
        
        result = requests.post(url, json = issueJson, headers = authHeaders)
        resultJson = json.loads(str(result.content.decode()))
        issueId = str(resultJson['issue']['id'])
        
        # issueId = str(545) # Debugging
        print("Eintrag erstellt: " + issueId)
        return issueId
        
# print(getIssueInfo(653)) # Debugging Purpose