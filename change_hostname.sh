#!/bin/bash
sudo su <<- ENDSU
	hostnamectl set-hostname $2
	sed -i "s/${1}/${2}/gI" /etc/hosts
ENDSU

echo "/etc/hostname"
cat /etc/hostname
echo "/etc/hosts"
cat /etc/hosts