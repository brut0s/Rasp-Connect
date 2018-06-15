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

print bcolors.WARNING + "\n[!]. Setting Up 'WPA' Wifi Connection" + bcolors.ENDC

ssid = raw_input(bcolors.WARNING + "\n[!]. Enter the 'SSID' of the WPA Network, you want to Connect to: ") + bcolors.ENDC

password = raw_input(bcolors.WARNING + "\n[!]. Enter the 'WPA' Password: ") + bcolors.ENDC

print bcolors.WARNING + "\nReplacing wpa_supplicant with New Config" + bcolors.ENDC 

#os.system('sudo rm /etc/wpa_supplicant/wpa_supplicant.conf')

net = """
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network = {
    ssid="%s"
    scan_ssid=1
    key_mgmt=WPA-PSK
    psk="%s"
}""" % (ssid, password)

filepath = "/etc/wpa_supplicant/wpa_supplicant.conf"

wifi = open(filepath, "w")
wifi.write(net)
wifi.close()

