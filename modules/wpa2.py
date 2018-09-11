#!/usr/bin/python
#
#
import os
import os.path
import sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"

print bcolors.WARNING + "\n" + bcolors.ENDC

ssid = raw_input("\nEnter the 'SSID' of the WPA2 Network, you want to Connect to: ")
password = raw_input("\nEnter the 'WPA2' Password: ")

print bcolors.WARNING + "\nReplacing wpa_supplicant with New Config" + bcolors.ENDC 

os.system('sudo rm /etc/wpa_supplicant/wpa_supplicant.conf')

net = """
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
	ssid="%s"
	psk="%s"
	key_mgmt=WPA-PSK
}

""" % (ssid, password)

filepath = "/etc/wpa_supplicant/wpa_supplicant.conf"

wifi = open(filepath, "w")
wifi.write(net)
wifi.close()
