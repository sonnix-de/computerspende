# Import the necessary packages
# https://pypi.org/project/simple-term-menu/
from consolemenu import *
from consolemenu.items import *
import readhw as hw


def showHardware():
    print(hw.getInformationAboutCurrentComputer())
    weiter = input()


def showHelp():
    hilfeText = """
    Dieses kleine Tool bietet ein paar Funktionen zum aussetzen der Rechner und 
    zum Einpflegen der Daten in Mantis.
    Außerdem bietet es noch die Möglichkeit ein Dokument für die Übergabe des 
    Computers ausdrucken zu können.
    """
    print(hilfeText)
    weiter = input("Weiter mit einer Taste")


def cleanHdd():
    print("welche Festplatte soll geputzt werden?")
    hdd = input('geben Sie den Namen der Festplatte ein')
    print(hdd)
    weiter = input('Weiter mit einer Taste')


# Create the menu
menu = ConsoleMenu("Computerspende Regensburg",
                   "Kleine Helferlein bei der Installation")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Infos über das Programm")
function_item1 = FunctionItem("Hilfe zum Programm", showHelp)
function_item2 = FunctionItem("Infos über den Computer", showHardware)
function_item3 = FunctionItem("Clean Hdd", cleanHdd)

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
# menu.append_item(menu_item)
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
# menu.append_item(command_item)
# menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
