#!/usr/bin/python3
import socket
import subprocess
import sys
from pyfiglet import Figlet
from datetime import datetime

#test
subprocess.call('clear', shell=True)
#Create banner from pyfiglet module
fig = Figlet()
ascii_banner = fig.renderText(" \\[T]/ \nMy First Port Scanner!\n \\[T]/ ")

print(ascii_banner)

print("Disclaimer! This program is intended for educational and ethical hacking purposes only! ")
print("Unauthorized port scanning without permission is intrusive and may be illegal. ")
print("Always make sure you have the right to scan the target system before hand.")


#user input with ip address, min to max port range

def user_target():
    while True:
        target = input("Enter target IP address: ")
        #Check to see if user input is valid
        try:
            target_ip = socket.gethostbyname(target)
            print(f"Loading up target {target_ip}")
            return target_ip
        except socket.error as e:
            print(f"Error: {e}")
            print("Input was invalid, please try again")


main_target = user_target()
port_min = int(input("Enter the minimum port range to scan in: "))
port_limit = int(input("Enter max port range to scan in: "))

#This function will scan the open ports of the target
def port_scanning(tar_ip, port):
#creating a socket variable
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

#Next in the function we will create a try statement to try to connect to port
    try:
        sock.connect((tar_ip, port))
        print(f"Port {port} is open!")
#If connection on the port failed or is closed
    except:
        pass
    finally:
        sock.close()


def scan_time(target_ip, startport, endport):
    try:
        times1 = datetime.now()
        print(f"Starting scan on {target_ip} at {times1}")
        for port in range(startport, endport):
           port_scanning(target_ip, port)
        times2 = datetime.now()
        total = times2 - times1
        print("---------------------------\n")
        print(f"Scan complete, took {total} amount of time")
    except KeyboardInterrupt:
        print("You have exited the program")
        sys.exit()

scan_time(main_target, port_min, port_limit)
