import psutil
import platform
import subprocess
from datetime import datetime


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
    SystemInfo = {}
    SystemInfo['System'] = uname.system
    SystemInfo['Node Name'] = uname.node
    SystemInfo['Release'] = uname.release
    SystemInfo['Version'] = uname.version
    SystemInfo['Machine'] = uname.machine
    SystemInfo['Prozessor'] = uname.processor
    return SystemInfo


def getCpu():
    SystemInfo = {}
    SystemInfo['Pysical Cores'] = psutil.cpu_count(logical=False)
    SystemInfo['Total cores'] = psutil.cpu_count(logical=True)
    return SystemInfo


def getInformationAboutCurrentComputer():
    mainInfo = {}
    mainInfo['SystemInfo'] = getSystemInformation()
    mainInfo['CPU'] = getCpu()
    return mainInfo

def cpu():
    return subprocess.check_output("grep -i 'model name' /proc/cpuinfo | uniq | awk -F': ' '{ print $2 }'", shell=True).decode().strip();

def memory():
    return subprocess.check_output("grep -i 'MemTotal' /proc/meminfo | awk '{ $2=int($2/1000000)\" GB\"; print$2 }'", shell=True).decode().strip();

