#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import requests

ports = []

def checkinternet(host="8.8.8.8", port=53, timeout=3):
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except socket.error as ex:
    print(ex)
    return False

def get_globalip():
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    return ip

def get_localip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def portscan(ip):
    remoteServer = ip

    print (">" * 60)
    print ("Scanning remote host", remoteServer)
    print ("<" * 60)

    try:
        for port in range(1,65535):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServer, port))
            if result == 0:
                print ("Port {}: 	 Open".format(port))
                ports.append(port)
            sock.close()
    except socket.error:
        print ("Can't connect to server")

def main():
    subprocess.call('clear', shell=True)
    print("="*24)
    print("P O R T   S C A N N E R")
    print("="*24)

    t1 = datetime.now()

    online = checkinternet()
    if(online==True):
        print("Host is connected to the internet...")
    else:
        print("Host is offline...")
    print()

    gIP = get_globalip()
    lIP = get_localip()
    print("Global ip: ", gIP)
    print("Local ip: ", lIP)
    print()

    portscan(gIP)
    portscan(lIP)

    t2 = datetime.now()
    time =  t2 - t1
    print()
    print("Time taken to complete scan: ", time)

main()