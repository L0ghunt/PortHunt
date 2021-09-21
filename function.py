import argparse
import socket
import os
import sys


def Logo():
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


def main():
    Sis()
    Logo()
    Argumentos()
    Conectar()


def Sis():
    if sys.platform != "linux2":
        os.system('cls')
    else:
        os.system('clear')


def Argumentos():
    global args
    print('\n[+] PortHunt1.0 by: L0gHunt \n')
    print('[+] Digite PortHunt.py --help para ver os comandos\n')
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='host', action='store', help='Use -s para definir o alvo EXEMPLO: PortHunt.py -s www.google.com')
    parser.add_argument('-P', dest='port', action='store', help='Use -P para definir uma porta especifica EXEMPLO: PortHunt.py -s www.google.com -P 80')
    parser.add_argument('-V', dest='version', action='version', version='%(prog)s 1.0 ')
    args = parser.parse_args()


def Conectar():
    if (args.host and args.port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        c = s.connect_ex((str(args.host),int(args.port)))
        if c == 0:
            print("\nPorta"+args.port+"\nAberta")
        else:
            print("\nPorta"+args.port+"\nFechada")
    else:
        quit


main()
