"""Lab Objective: Create a program that can detect active ARP Spoofing attacks on host machines."""
import os
import time
from datetime import datetime

# The function accesses the ARP table and extracts its entries.
def arp_table_extraction():
    # Read the ARP table and save it in a list form.
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    # A dictionary to hold IP addresses with corresponding MAC addresses.
    addresses = {}
    # Iterating over the ARP entries list, filtering unnecessary data and saving IP & MAC addresses into a dictionary.
    for line in arp_table_lines:
        if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
            break
        if arp_table_lines.index(line) > 2:
            ip, mac, _type = line.split()
            addresses[ip] = mac

    identify_duplication(addresses)

# The function examines the IP & MAC addresses dictionary and checks it for MAC duplication.
def identify_duplication(addresses):
    # Temporary list to save iterated MAC addresses for later comparison.
    tmp_mac_lst = []
    print("Scanning...")
    time.sleep(3)
    for mac in addresses.values():
        # Terminates the iteration if a MAC duplication was found.
        if mac in tmp_mac_lst:
            print("Finished scanning")
            create_log("Arp Spoofed!\nThe address is:" + mac)
            break
        tmp_mac_lst.append(mac)

# This function creates a file and append into it a log of the ARP spoofing event.
def create_log(message):
    print("Generating logs...")
    time.sleep(3)
    date = datetime.now()
    with open("log.txt", "a") as log:
        log.write(message + "\nDate: {}\n\n".format(date))
    print("The event is logged in log.txt")

# A condition to verify that this file is directly executed.
if __name__ == "__main__":
    arp_table_extraction()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
