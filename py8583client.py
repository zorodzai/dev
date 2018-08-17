#!usr/bin/env python
import socket
import xml.etree.ElementTree as ET

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_address = ('localhost',10001)
listen_socket.bind(listen_address)
print('Listening...')

while(True):
    reply = listen_socket.recvfrom(4096)
    print(reply)

