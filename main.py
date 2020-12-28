# Import the necessary packages
# https://pypi.org/project/simple-term-menu/
from consolemenu import *
from consolemenu.items import *

import readhw as hw


def showHardware():
    print(hw.getInformationAboutCurrentComputer())
    input()


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
    print("welche Festplatte soll geputzt werden?")
    hdd = input('geben Sie den Namen der Festplatte ein')
    print(hdd)
    input('Weiter mit enter')


def createAsset():
    print("Der Mantis-Eintrag wird erstellt")
    input('Weiter mit enter')


# Create the menu
menu = ConsoleMenu("Computerspende Regensburg",
                   "Kleine Helferlein bei der Installation")

function_item1 = FunctionItem("Hilfe zum Programm", showHelp)
function_item2 = FunctionItem("Infos über den Computer", showHardware)
function_item3 = FunctionItem("Clean Hdd", cleanHdd)
function_item4 = FunctionItem("Asset (Mantis) erstellen", createAsset)

menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)

menu.show()
