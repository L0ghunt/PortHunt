import argparse
import socket
import os
import sys


def PortHuntlogo():
    print('''
 _______  _______  _______ _________                   _       _________
(  ____ )(  ___  )(  ____ )\__   __/|\     /||\     /|( (    /|\__   __/
| (    )|| (   ) || (    )|   ) (   | )   ( || )   ( ||  \  ( |   ) (   
| (____)|| |   | || (____)|   | |   | (___) || |   | ||   \ | |   | |   
|  _____)| |   | ||     __)   | |   |  ___  || |   | || (\ \) |   | |   
| (      | |   | || (\ (      | |   | (   ) || |   | || | \   |   | |   
| )      | (___) || ) \ \__   | |   | )   ( || (___) || )  \  |   | |   
|/       (_______)|/   \__/   )_(   |/     \|(_______)|/    )_)   )_(1.0  
                                                                        
    ''')

def escolhas():
    print("   Nmap scan for: %s\n" % target)
    print("   {1}--Simple Scan [-sV]")
    print("   {2}--Port Scan [-Pn]")
    print("   {3}--Operating System Detection [-A]\n")
    print("   {99}-Return to information gathering menu \n")
    response = raw_input("nmap ~# ")
    clearScr()
    logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    try:
        if response == "1":
            os.system("nmap -sV -oN %s %s" % (logPath, target))
            response = raw_input(continuePrompt)
        elif response == "2":
            os.system("nmap -Pn -oN %s %s" % (logPath, target))
            response = raw_input(continuePrompt)
        elif response == "3":
            os.system("nmap -A -oN %s %s" % (logPath, target))
            response = raw_input(continuePrompt)
        elif response == "99":
           quit == "99"
