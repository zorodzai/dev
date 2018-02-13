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
    if bigEndian:
        try:
            message=iso.getNetworkISO()
            s.send(message)
            print('Sending ... %s' % message)
            ans=s.recv(2048)
            print("\nInput ASCII |%s|" % ans)
            isoAns = ISO8583()
            isoAns.getNetworkISO(ans)
            v1=isoAns.getBitsAndValues()
            for v in v1:
                print("Bit %s of type %s with value = %s" % (v['bit'],v['type'],v['value']))
                
            if isoAns.getMTI()=='0810':
                print("\nThat's great. Server understood message")
            else:
                print("\nError in parsing message")
            
        except InvalidISO8583,ii:
            print ii
            break
            
        time.sleep(timeBetweenEcho)
    else:
        try:
            message = iso.getNetworkISO(False)
            s.send(message)
            print('Sending ... %s' % message)
            ans = s.recv(2048)
            print("\nInput ASCII |%s|" % ans)
            isoAns = ISO8583()
            isoAns.setNetworkISO(ans,False)
            v1 = isoAns.getBitsAndValues()
            for v in v1:
                print("Bit %s of type %s with value = %s" % (v['bit'],v['type'],v['value'])))
            
            if isoAns.getMTI=='0810':
                print("\nManaged to parse correctly")
            else:
                print("error parsing message")
                
        except InvalidISO8583, ii:
            print ii
            break
            
        time.sleep(timeBetweenEcho)
        
print("Closing")
s.close()
