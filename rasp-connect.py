#!/usr/bin/python
#
#
import os
import sys

class bcolors:

    ENDC = '\033[0m'
    RED   = "\033[1;31m"
    GREEN = "\033[0;32m"
    WARNING = "\033[93m"
	
	
print """
 ____                        ____                            _   
|  _ \ __ _ ___ _ __        / ___|___  _ __  _ __   ___  ___| |_ 
| |_) / _` / __| '_ \ _____| |   / _ \| '_ \| '_ \ / _ \/ __| __|
|  _ < (_| \__ \ |_) |_____| |__| (_) | | | | | | |  __/ (__| |_ 
|_| \_\__,_|___/ .__/       \____\___/|_| |_|_| |_|\___|\___|\__|
               |_|  

"""
		
def print_menu():
    print "-----------------------------------------------"
    print "Select One of the Following Wireless Encryption"
    print "###############################################"
    print bcolors.WARNING + "[1]. NONE (OPEN)"
    print "[2]. WEP"
    print "[3]. WPA"
    print "[4]. WPA2"
    print "[5]. View Sample for wpa_supplicant.conf"
    print "[6]. Exit" + bcolors.ENDC
    print "################################################"
    print "------------------------------------------------"

loop=True

while loop:
    print_menu()
    choice = input(bcolors.WARNING + "\nSelect an Option [1-6]: " + bcolors.ENDC)

    if choice==1:

	import clear
	import modules.open
	import clear


    elif choice==2:

	import clear
	import modules.wep
	import clear


    elif choice==3:

	import clear
        import modules.wpa
        import clear


    elif choice==4:

	import clear
	import modules.wpa2
	import clear


    elif choice==5:


        import modules.wpa_supplicant
        cont = raw_input(bcolors.WARNING + "\n[!]...Press 'Return' to Continue") + bcolors.ENDC
	import clear



    elif choice==6:

        print bcolors.GREEN + "\nThanks for using Rasp-Connect" + bcolors.ENDC
        loop=False


    else:

        raw_input(bcolors.RED + "\n[!]-Error That was a invalid Number, \n\nSelect from [1-6]" + bcolors.ENDC)
