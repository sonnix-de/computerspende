import psutil
import platform
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
    SystemInfo['Sytem'] = uname.system
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


"""
Main Program
"""

mainInfo = {}
mainInfo['SystemInfo'] = getSystemInformation()
mainInfo['CPU'] = getCpu()
si = getSystemInformation()
print (mainInfo)
