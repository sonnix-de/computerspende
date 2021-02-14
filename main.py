# Import the necessary packages
# https://pypi.org/project/simple-term-menu/
from consolemenu import *
from consolemenu.items import *
import cleanhdd as cleanhdd
import IssueBuilder as IssueBuilder
import issues as issues
import subprocess
import os

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
    issueId = issues.createIssue(issue)
    old_hostname = subprocess.check_output("hostname", shell=True).decode().strip()
    new_hostname = 'CSR' + str(issueId)
    subprocess.run(['hostnamectl', 'set-hostname', new_hostname])
    print('Hostname von ' +  old_hostname + ' zu ' + new_hostname + ' geändert.')
    input('Weiter mit enter')


def updateAsset():
    print("Der Mantis-Eintrag wird aktualisiert (id muss übergeben werden)")
    input('Weiter mit enter')
    

# Create the menu
menu = ConsoleMenu("Computerspende Regensburg",
                   "Kleine Helferlein bei der Installation")

function_item1 = FunctionItem("Hilfe zum Programm", showHelp)
function_item2 = FunctionItem("Infos über den Computer", showHardware)
function_item3 = FunctionItem("Clean Hdd", cleanHdd)
function_item4 = FunctionItem("Asset (Mantis) erstellen", createAsset)
function_item5 = FunctionItem("Asset (Mantis) aktualisieren", updateAsset)

menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)
menu.append_item(function_item5)

menu.show()
