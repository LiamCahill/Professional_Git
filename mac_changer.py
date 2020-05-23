#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    #The subprocess module takes in strings, runs them as commands through the terminal.

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","eth0",new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    #The optparse module is depeicated at the time of taking this class.
    #According to Python Docs. page, it is replaced by argparse module.

parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address.")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(option, arguments) = parser.parse_args()


change_mac(option.interface, option.new_mac)


