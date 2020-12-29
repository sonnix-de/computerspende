import psutil
import platform
import subprocess
from datetime import datetime
import cv2

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getSystemInformation():
    """
    Nur ein Kommentar
    """
    uname = platform.uname()
    system_info = {}
    system_info['System'] = uname.system
    system_info['Node Name'] = uname.node
    system_info['Release'] = uname.release
    system_info['Version'] = uname.version
    system_info['Machine'] = uname.machine
    system_info['Prozessor'] = uname.processor
    return system_info


def getCpu():
    system_info = {'Pysical Cores': psutil.cpu_count(logical=False), 'Total cores': psutil.cpu_count(logical=True)}
    return system_info


def getInformationAboutCurrentComputer():
    main_info = {'SystemInfo': getSystemInformation(), 'CPU': getCpu()}
    return main_info


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
