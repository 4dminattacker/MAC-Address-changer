# hello Developers
# import library
import subprocess
import optparse
import re

# parser
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="network_interface", help="Specify the network interface.")
parser.add_option("-m", "--mac", dest="new_mac_address", help="Specify the new MAC address.")
options, arguments = parser.parse_args()

if not options.network_interface:
    print("[-] Error: Please specify the network interface using -i or --interface.")
    exit()

if not options.new_mac_address:
    print("[-] Error: Please specify the new MAC address using -m or --mac.")
    exit()

# change MAC
print("[~] Changing MAC address...")
subprocess.call(f"ifconfig {options.network_interface} down", shell=True)
subprocess.call(f"ifconfig {options.network_interface} hw ether {options.new_mac_address}", shell=True)
subprocess.call(f"ifconfig {options.network_interface} up", shell=True)

# filtering MAC Address
result = subprocess.check_output(f"ifconfig {options.network_interface}", shell=True).decode("UTF-8")
search_mac = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result)

if search_mac:
    print(f"[+] MAC address changed to: {search_mac.group(0)}")
else:
    print("[-] Error: MAC Address not found.")

