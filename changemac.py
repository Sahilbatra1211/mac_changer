#!/user/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC")
    parser.add_option("-m", "--mac", dest="newMac", help="new Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("No interface given,please refer --help for complete arguments")
    elif not options.newMac:
        parser.error("No mac given,please refer --help for complete arguments")
    else:
        return (options, arguments)


def change_mac(interface, newMAc):
    print("Changing mac of " + interface + " to " + newMac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    # print("ifconfig " + interface + " hw ether " + newMac)
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


(options, arguments) = get_arguments()

interface = options.interface
# interface = input("interface > ")
newMac = options.newMac
# newMac = input("newMac > ")

change_mac(interface, newMac)
