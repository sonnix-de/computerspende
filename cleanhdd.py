"""
   Zeigt die vorhandenen devices mit einem OS Befhehl an, 
   schlägt den shred-befehl vor und kann ihn auch ausführen.
   
   Diese Modul kann über das Main Menu aufgerufen werden.
"""

import os, subprocess


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
    device = input('Bitte geben sie das device zum shredden an (z.B. sda oder sdb): ')
    if subprocess.check_output("cat /sys/block/" + device + "/queue/rotational",
                                shell=True).decode().strip() == "1":
        delete_hdd(device)
    elif subprocess.check_output("cat /sys/block/" + device + "/queue/rotational",
                                shell=True).decode().strip() == "0":
        delete_ssd(device)

def delete_ssd(device):
    output = subprocess.check_output("sudo hdparm -I /dev/" + device, shell=True).decode().splitlines() 
    if "not frozen" in output:
        pass
    elif "frozen" in output:
        print("SSD is frozen. I will try to put it to sleep. If the device does a restart and not waking up again. You have to open the case of device, start the system, remove the SSD for a short time > 1 sec from the connector, reconnect it and start the process again.")
        subprocess.check_output("sudo systemctl suspend", shell=True).decode().splitlines()
    print("I will set a password for the device")
    subprocess.check_output("sudo hdparm --user-master u --security-set-pass GEHEIM /dev/" + device, shell=True).decode().splitlines() 
    output = subprocess.check_output("sudo hdparm -I /dev/" + device, shell=True).decode().splitlines() 
    if "Master password revision code" in output and not "not enabled" in output:
        print("ATTENTION: WILL DELETE ALL DATA!! Password is set. I will erase the SSD now.")
        msg = os.system("sudo time hdparm --user-master u --security-erase GEHEIM /dev/" + device)
        print(msg)
        output = subprocess.check_output("sudo hdparm -I /dev/" + device, shell=True).decode().splitlines() 
        if "not enabled" in output:
            print("Everything went fine. The SSD is now deleted.")
        else:
            print("Something went wrong. Try again")
    else:
        print("Something went wrong. Try again")


def delete_hdd(device):
    command = "sudo shred -v -n 0 -z /dev/" + device
    print(command)
    weiter = input('Soll der Befehl ausgeführt werden? (y,n)')
    if weiter == "Y" or weiter == 'y':
        msg = os.system(command)
        print(msg)
    input('Weiter mit Enter')


# für einen internen test:
# excuteMenueItem()
