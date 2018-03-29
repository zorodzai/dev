#!usr/bin/env python

import socket
import sys
import struct
import os
from py8583.py8583 import Iso8583, MemDump, Str2Bcd
from py8583.py8583spec import IsoSpec1987BCD

serverIP = socket.gethostname()
serverPort = 26000
s = socket.socket()

while True:
    try:
        s.connect((serverIP,serverPort))
        print("connected")
        #print(s.recv(1024))
        
        IsoPacket.MTI("0800")
        IsoPacket.Field(7,1)
        IsoPacket.FieldData(7,"0213141501")
        IsoPacket.Field(11,1)
        IsoPacket.FieldData(11,"123456")
        IsoPacket.Field(12,1)
        IsoPacket.FieldData(12,"141501")
        IsoPacket.Field(13,1)
        IsoPacket.FieldData(13,"0213")
        IsoPacket.Field(70,1)
        IsoPacket.FieldData(70,"301")

        IsoPacket.PrintMessage()
        data=IsoPacket.BuildIso()
        data=struct.pack("!H",len(data))+data
        MemDump("Sending: ", data)
        s.send(data)
    except socket.error:
        s.close()
        s=None
        continue
    break
    if s is None:
        print("COuld not connect")
        sys.exit(1)
    


s.close()

    
    
    

