import socket
import colorama
from colorama import init, Fore 

init()

GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX-


def is_port_open(host, port):
    sock = socket.socket()
    try:
  
        sock.settimeout(1)
        sock.connect((host,port))
        return True
    except:     
        return False
    finally:
        sock.close()

host = input("Enter Host: ")

for port in range(1,1025):
    if is_port_open(host, port):
        print(f"{GREEN} [+] {host}:{port} is open {RESET}")

    else:
        print(f"{GRAY} [!] {host}:{port} is closed {RESET}")
        
    


