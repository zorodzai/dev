#!/usr/bin/python
import socket
import sys
import time
from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

serverIP = socket.gethostname()
serverPort = 26000
numberEcho = 10
timeBetweenEcho = 5

bigEndian = True
s = None

for res in socket.getaddrinfo(serverIP,serverPort,socket.AF_UNSPEC,socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except socket.error, msg:
        s=None
        continue
    try:
        s.connect(sa)
    except socket.error, msg:
        s.close()
        s=None
        continue
    break
if s is None:
    print("Could not connect")
    sys.exit(1)
    
for req in range(0,numberEcho):
    iso = ISO8583()
    iso.SetMTI('0800')
    iso.setBit(7,'0213141501')
    iso.setBit(11,'123456')
    iso.setBit(12,'141501')
    iso.setBit(13,'0213')
    iso.setBit(70,'301')
