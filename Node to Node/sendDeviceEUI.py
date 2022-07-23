from network import LoRa
import socket
import time
import ubinascii
import struct
import machine
import uos
import pycom
import sys

from pysense import Pysense
from SI7006A20 import SI7006A20 # Temperature sensor


py = Pysense()
si = SI7006A20(py)

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
humidity = str(si.humidity())

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
devEUI = ubinascii.hexlify(lora.mac()).upper().decode('utf-8')
i = 0
while True:
    otherNodeEUI = s.recv(64).decode("utf-8");
    print(otherNodeEUI);
    s.send('Hi from Node 1. My ID is ' + devEUI + ' and my humidity is ' + humidity);
    # if s.recv(64) == b'Ping':
    #     s.send('Pong')
    #     print('Pong {}'.format(i))
    #     i = i+1
    # print('Recieved Node EUI is ' + otherNodeEUI)
    time.sleep(5)

