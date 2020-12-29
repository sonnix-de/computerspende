"""
   Zeigt die vorhandenen devices mit einem OS Befhehl an, 
   schlägt den shred-befehl vor und kann ihn auch ausführen.
   
   Diese Modul kann über das Main Menu aufgerufen werden.
"""

import os


def excuteMenueItem():
    info = """
    Dieser Befehl liest die angeschlossenen Laufwerke aus und frägt nach dem zu löschenden Laufwerk.
    Nach der Eingabe dieses Laufwerk, wird der zugehörige shred Befehl vorgeschlagen, um die Festplatte zu "putzen"
    ---
    Dieser Befehl kann dann entsprechend kopiert und ausgeführt werden (auf eigene Verantwortung)
    """
    print(info)
    command = os.popen('sudo lshw -short -C disk')
    msg = command.read()
    print(msg)
    device = input(
        'Bitte geben sie das device zum shredden an (z.B. sda oder sdb): ')
    command = "sudo shred -v -n 0 -z /dev/"+device
    print(command)
    # ist noch zur sicherheit umgebaut...
    command = "find "
    print(command)
    # pv wäre evtl. auch eine option print("sudo pv -v -n 0 -z /dev/"+device)
    weiter = input('Soll der Befehl ausgeführt werden? (y,n)')
    if weiter == "Y" or weiter == 'y':
        msg = os.system(command)
        print(msg)
    input('Weiter mit Enter')


# für einen internen test:
# excuteMenueItem()
