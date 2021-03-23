import psutil
import platform
import subprocess
from datetime import datetime
import cv2
import json


def get_size(bytes, suffix="B", separator=","):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB' or '1,17 GB depending on the separator default is ,
    """
    factor = 1024
    bytes = int(bytes)
    suffix = "B"
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            if separator == ",":
                return f"{bytes:.2f} {unit}{suffix}".replace('.',',')
            elif separator == ".":
                return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor


def cpu():
    cpu = subprocess.check_output("grep -i 'model name' /proc/cpuinfo | uniq | awk -F': ' '{ print $2 }'", shell=True).decode().strip();
    # wir können etwas kürzen damit die werte nicht zu lang werden
    # hier kann man einfach weiter ergänzen für andere CPU Modelle
    return cpu.replace('Intel(R) Core(TM) ', '')


def memory():
    bytes = subprocess.check_output("grep -i 'MemTotal' /proc/meminfo | awk '{ print$2; }'", shell=True).decode().strip();
    return f"{(float(bytes) / 1024 / 1024):.2f}" + " GB"
    
    
def check_for_cam(cam=0):
    cap = cv2.VideoCapture(cam)
    if cap is None or not cap.isOpened():
        return "Nein"
    else:
        return "Ja"


def storage():
    devices=subprocess.check_output("lsblk -o Name -p -l -n", shell=True).decode().splitlines()
    for device in devices:
        # wir brauchen nur nach SD (Sata Device) und NVME suchen, devices wie loop etc interessieren nicht
        if ("/dev/sd" in device) or ("/dev/nvme" in device):
                type = "SSD"
                # nvme wird sich nicht merh drehen denke ich
                if "/dev/sd" in device:
                    if subprocess.check_output("cat /sys/block/" + device.split("/")[2] + "/queue/rotational", shell=True).decode().strip() == "1":
                        type = "HDD"
                    
                return get_size(subprocess.check_output("lsblk -b " + device + " -o SIZE -n -d", shell=True), "G") + " (" + type + ")"
    
    # keine der platten ist eine SD oder NVME
    return "Keine Ahnung"

def usb3():
    try:
        lsusb = subprocess.check_output("sudo lsusb", shell=True).decode()
    except subprocess.CalledProcessError:
        return "Exitcode 1, läuft grad in ner WSL zum testen?" # Zu debugging Zwecken ist dies hier enthalten
    if "3.0 root hub" in lsusb:
        return "Ja"
    else:
        return "Nein"

def graphicscard():
    lshw = subprocess.check_output("sudo -S lshw -json -C display -quiet", shell=True).decode()
    try:
        lshwJson = json.loads(str(lshw))[0]
    except IndexError:
        return "IndexError, läuft grad in ner WSL zum testen?" # Zu debugging Zwecken ist dies hier enthalten
    
    return lshwJson.get("product") + " (" + lshwJson.get("vendor") + ")"   

def wifi():
    
    lshw = subprocess.check_output("sudo lshw -quiet", shell=True).decode()
    
    if "802.11" in lshw:
        return "Ja"
    else:
        return "Nein"