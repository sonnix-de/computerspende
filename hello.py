import os

command = os.popen('sudo lshw -class cpu')
msg = command.read()
print(msg)
command.close()
