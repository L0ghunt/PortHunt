import socket
import os


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

def scan_ports(host):
    open_ports = []
    for port in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port)
                open_ports.append((port, service))
    return open_ports

def main():
    host = input("Digite o host a ser escaneado: ")

    print(f"Escaneando todas as portas em {host}...")
    open_ports = scan_ports(host)

    if open_ports:
        print("Portas abertas:")
        for port, service in open_ports:
            print(f"Porta: {port}\tServiço: {service}")
    else:
        print("Nenhuma porta aberta encontrada.")

if __name__ == "__main__":
    main()

