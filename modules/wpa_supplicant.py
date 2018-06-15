#!/usr/bin/python
#
#

print """
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
####################################
# Sample Config for wpa_supplicant #
#                                  #
#        Path to Config:           #
#   /etc/network/wpa_supplicant    #
####################################

# Example Open

network={
    ssid=""
    scan_ssid=1
    key_mgmt=NONE
}


# Example WEP

network={
    ssid=""
    scan_ssid=1
    key_mgmt=NONE
    wep_key0=""
}


# Example WPA

network={
    ssid=""
    scan_ssid=1
    key_mgmt=WPA-PSK
    psk=""
}


# Example WPA2

network={
    ssid=""
    scan_ssid=1
    proto=RSN
    key_mgmt=WPA-PSK
    psk=""
}

"""
