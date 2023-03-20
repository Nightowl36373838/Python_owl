"""MAC CHANGER"""
import subprocess
import optparse


def change_mac(interface, new_mac):
    print("[+] Changing MAC ADDRESS for Interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "wlan0", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify your Interface, Use --help for Usage")
    parser.add_option("-m", "--mac_address", dest="new_mac", help="Specify the New Mac_Address, Use --help for Usage")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify your Interface, Use --help for Usage")
    elif not options.new_mac:
        parser.error("[+] Please specify your New Mac Address, Use --help for Usage")
    return options


options = get_arguments()
change_mac(options.interface, options.new_mac)
