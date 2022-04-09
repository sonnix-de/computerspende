# Import the necessary packages
# https://pypi.org/project/simple-term-menu/

from config import readConfig # checks if a config.json file is available, if not creates one
readConfig()

from consolemenu import *
from consolemenu.items import *
import cleanhdd as cleanhdd
import IssueBuilder as IssueBuilder
import issues as issues
import subprocess
import os
import requests
import time

def showHardware():
    showHardware = os.system("sudo lshw -short -quiet")
    print(showHardware)


def showHelp():
    help_text = """
    Dieses kleine Tool bietet ein paar Funktionen zum aussetzen der Rechner und 
    zum Einpflegen der Daten in Mantis.
    Außerdem bietet es noch die Möglichkeit ein Dokument für die Übergabe des 
    Computers ausdrucken zu können.
    """
    print(help_text)
    input("Weiter mit enter")


def cleanHdd():
    cleanhdd.excuteMenueItem()


def createAsset():
    issue = IssueBuilder.build()
    # issueId = 545 # Debugging
    # print (issueId) # Debugging
    issueId = issues.createIssue(issue)
    old_hostname = subprocess.check_output("hostname", shell=True).decode().strip()
    new_hostname = 'CSR' + str(issueId)
    subprocess.call(['sh', 'change_hostname.sh', old_hostname, new_hostname])
    print('Hostname sowohl in der /etc/hostname als auch in der /etc/hosts Datei von ' + old_hostname + ' zu ' + new_hostname + ' geändert.')
    input('Weiter mit enter')


def updateAsset():
    print("Der Mantis-Eintrag wird aktualisiert (id muss übergeben werden)")
    input('Weiter mit enter')


def servicecheck():
    main_site = requests.get("https://computerspende-regensburg.de")
    cloud = requests.get("https://cloud.computerspende-regensburg.de")
    mantis = requests.get("https://assets.computerspende-regensburg.de")
    tickets = requests.get("https://tickets.computerspende-regensburg.de")
    if main_site.status_code == 200:
        print(f"Main Seite funktioniert  ({main_site.elapsed.total_seconds()})s")
    else:
        print(f"Main Seite funktioniert NICHT  ({main_site.status_code}) ")
    if cloud.status_code == 200:
        print(f"Nextcloud funktioniert ({cloud.elapsed.total_seconds()})s")
    else:
        print(f"Nextcloud funktioniert NICHT   ({cloud.status_code}) ")
    if mantis.status_code == 200:
        print(f"Mantis Tracker funktioniert  ({mantis.elapsed.total_seconds()})s")
    else:
        print(f"Mantis Tracker funktioniert NICHT  ({mantis.status_code}) ")
    if tickets.status_code == 200:
        print(f"Ticket System funktioniert  ({tickets.elapsed.total_seconds()})s")
    else:
        print(f"Ticket System funktioniert NICHT ({tickets.status_code}) ")

    time.sleep(4)


# Create the menu
menu = ConsoleMenu("Computerspende Regensburg",
                   "Kleine Helferlein bei der Installation")

function_item1 = FunctionItem("Hilfe zum Programm", showHelp)
function_item2 = FunctionItem("Infos über den Computer", showHardware)
function_item3 = FunctionItem("Clean Hdd", cleanHdd)
function_item4 = FunctionItem("Asset (Mantis) erstellen", createAsset)
function_item5 = FunctionItem("Asset (Mantis) aktualisieren", updateAsset)
function_item6 = FunctionItem("Service-Checker", servicecheck)

menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)
menu.append_item(function_item5)
menu.append_item(function_item6)

menu.show()
