
# Postinstallation script with additional software and settings

# Teamviewer
wget https://download.teamviewer.com/download/linux/signature/TeamViewer2017.asc
sudo apt-key add TeamViewer2017.asc
sudo sh -c 'echo "deb http://linux.teamviewer.com/deb stable main" >> /etc/apt/sources.list.d/teamviewer.list'
sudo apt -y update
sudo apt -y install teamviewer

