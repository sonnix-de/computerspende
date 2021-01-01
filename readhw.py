import psutil
import platform
import subprocess
from datetime import datetime
import cv2

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
    return subprocess.check_output("grep -i 'MemTotal' /proc/meminfo | awk '{ $2=int($2/1000000)\" GB\"; print$2 }'", shell=True).decode().strip();

def check_for_cam(cam=0):
    cap = cv2.VideoCapture(cam)
    if cap is None or not cap.isOpened():
        return "Nein"
    else:
        return "Ja"


def storage():
    devices=subprocess.check_output("lsblk -o Name -p -l -n", shell=True).decode().splitlines()
    for device in devices:
        if "nvme" in device:
            if subprocess.check_output("cat /sys/block/nvme/queue/rotational", shell=True).decode().strip() == 1:
                type = "HDD"
            else:
                type = "SSD"
            return get_size(subprocess.check_output("lsblk -b /dev/nvme0n1 -o SIZE -n -d", shell=True), "G") + " (" + type + ")"
        elif "sda" in device:
            if subprocess.check_output("cat /sys/block/sda/queue/rotational", shell=True).decode().strip() == 1:
                type = "HDD"
            else:
                type = "SSD"
            return get_size(subprocess.check_output("lsblk -b /dev/sda -o SIZE -n -d", shell=True), "G") + " (" + type + ")"
        elif "vda" in device:
            if subprocess.check_output("cat /sys/block/vda/queue/rotational", shell=True).decode().strip() == 1:
                type = "HDD"
            else:
                type = "SSD"
            return get_size(subprocess.check_output("lsblk -b /dev/vda -o SIZE -n -d", shell=True), "G") + " (" + type + ")"


def wifi():
    lspci = subprocess.check_output("lspci").decode()
    if "Wireless" in lspci:
        return "Ja"
    else:
        return "Nein"
